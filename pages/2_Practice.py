import streamlit as st
from code_editor import code_editor
import ast
import builtins

from streamlit_local_storage import LocalStorage
from utils.scenarios import generated_scenarios

st.set_page_config(
    page_title="Python | Skill Test",
    page_icon=":snake:",
    layout="wide",
)


FINISHED_KEY = 'practice_finished'
def LocalStorageManager():
    return LocalStorage()
localS = LocalStorageManager()
current_filter = st.session_state.get("practice_filter", {})


st.session_state[FINISHED_KEY] = localS.getItem(FINISHED_KEY) or {}

scenarios = list(filter(lambda f: f["difficulty"] == current_filter["difficulty"] if "difficulty" in current_filter else True, sorted(generated_scenarios, key=lambda x: x["difficulty"])))

def get_current_code():
    finished_code = st.session_state.get(FINISHED_KEY, {}).get(st.session_state['current_scenario']['title'])
    return finished_code or st.session_state['current_scenario'].get('initial_code', "")
st.session_state.setdefault('current_scenario', scenarios[0])
st.session_state.setdefault('current_code',get_current_code())

def is_scenario_finished(scenario_title):
    return scenario_title in st.session_state[FINISHED_KEY].keys()

def save_current_code(code):
    st.session_state["current_code"] = code

current_scenario = st.session_state['current_scenario']

def translate_difficulty(difficulty):
    if difficulty == 1:
        return "Easy"
    elif difficulty == 2:
        return "Medium"
    elif difficulty == 3:
        return "Hard"
    else:
        return "Unknown"
st.sidebar.button("Reset Progress",
                  on_click=lambda: localS.setItem(FINISHED_KEY, {}), 
                  disabled=not bool(st.session_state[FINISHED_KEY]))

def update_filter(p_filter, difficulty):
    if "difficulty" in p_filter and p_filter["difficulty"] == difficulty:
        p_filter = {}
    else:
        p_filter = {"difficulty": difficulty}
    st.session_state.update(practice_filter=p_filter)

side_col1, side_col2, side_col3 = st.sidebar.columns(3)
with side_col1:
    st.button(f"{"✅" if current_filter.get("difficulty") == 1 else ""}Easy", use_container_width=True, on_click=lambda: update_filter(current_filter, 1))
with side_col2:
    st.button(f"{"✅" if current_filter.get("difficulty") == 2 else ""}Medium", use_container_width=True, on_click=lambda: update_filter(current_filter, 2))
with side_col3:
    st.button(f"{"✅" if current_filter.get("difficulty") == 3 else ""}Hard", use_container_width=True, on_click=lambda: update_filter(current_filter, 3))

st.sidebar.write("## Scenarios")
for scenario in scenarios: 
    st.sidebar.button(f"{"✅ " if is_scenario_finished(scenario["title"]) else ""}{translate_difficulty(scenario["difficulty"])} - {scenario["title"]}", 
                      key=f"{scenario["title"]}_sidebar", use_container_width=True, on_click=lambda s=scenario: st.session_state.update(current_scenario=s))


successful = False

scenario_title = current_scenario["title"]

st.title(scenario_title)


col1, col2 = st.columns(2)
with col1:
    st.write("Hit Ctrl + Enter to run the code in the editor below.")
    st.markdown(
        current_scenario["description"]
    )


with col2:
    response_dict = code_editor(get_current_code(), height=[10, 30], lang="python", key=scenario_title)


def validate_code_for_security(code):
    dangerous_nodes = (
        ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal,
        ast.With, ast.AsyncWith, ast.Lambda, ast.Try, ast.Raise
    )
    dangerous_names = {"exec", "eval", "open", "compile", "input", "__import__", "os", "sys", "subprocess"}

    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, dangerous_nodes):
                raise ValueError("Code contains potentially dangerous statements.")
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id in dangerous_names:
                    raise ValueError(f"Use of '{node.func.id}' is not allowed.")
                if isinstance(node.func, ast.Attribute) and node.func.attr in dangerous_names:
                    raise ValueError(f"Use of '{node.func.attr}' is not allowed.")
            if isinstance(node, ast.Name) and node.id in dangerous_names:
                raise ValueError(f"Use of '{node.id}' is not allowed.")
    except Exception as e:
        raise ValueError(f"Security validation failed: {e}")
    return code

def validate_no_override_builtins(code):
    predefined_names = set(dir(builtins))
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in predefined_names:
                raise ValueError(f"Overriding built-in name '{node.name}' is not allowed.")
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in predefined_names:
                        raise ValueError(f"Overriding built-in name '{target.id}' is not allowed.")
    except Exception as e:
        raise ValueError(f"Predefined name override validation failed: {e}")
    return code

def is_code_meet_optional_restriction(code, goal):
    if "max_lines" in goal:
        lines = [line for line in code.splitlines() if line.strip() and not line.strip().startswith("#") and not line.strip().startswith("def ")]
        if len(lines) > goal["max_lines"]:
           return False
    return True

if response_dict["text"]:
    save_current_code(response_dict["text"])
    try:
        code = response_dict["text"]
        validate_code_for_security(code)
        validate_no_override_builtins(code)
        exec(code, globals())
        errors = 0
        if "test_setup_code" in current_scenario:
            try:
                exec(current_scenario["test_setup_code"], globals())
            except Exception as e:
                raise ValueError(f"Test setup code execution failed: {e}")
        if current_scenario["function_name"] in globals():
            function = globals()[current_scenario["function_name"]]
            for test_case in current_scenario["test_cases"]:
                input_data = test_case["input"]
                if isinstance(input_data, dict):
                    result = function(**input_data)
                else:
                    result = function(*input_data)
                expected_output = test_case["expected_output"]
                if result != expected_output:
                    errors += 1
                    st.error(f"Test failed for input {input_data}. Expected {expected_output}, got {result}.")
                else:
                    st.success(f"Test passed for input {input_data}. Result: {result}.")
            if errors == 0 and "optional_code_goal" in current_scenario:             
                if is_code_meet_optional_restriction(code, current_scenario["optional_code_goal"]):
                    st.success("Your code meets the optional restrictions.")
                else:
                    st.warning(f"Your code does not meet the optional restrictions, expected at most {current_scenario['optional_code_goal']['max_lines']} lines of code to be used")
            if errors == 0:
                st.success("All tests passed successfully!")
                if scenario_title not in st.session_state[FINISHED_KEY]:
                    st.session_state[FINISHED_KEY][scenario_title] = response_dict["text"]
                    localS.setItem(FINISHED_KEY, st.session_state[FINISHED_KEY])
                st.rerun()
        else:
            st.error("Function 'add_numbers' not found.")
    except Exception as e:
        # pass
        st.error(f"Error executing code: {e}")