import streamlit as st
from code_editor import code_editor
import ast
import builtins

from streamlit_local_storage import LocalStorage

st.set_page_config(
    page_title="Python | Skill Test",
    page_icon=":snake:",
    layout="wide",
)


FINISHED_KEY = 'practice_finished'
def LocalStorageManager():
    return LocalStorage()
localS = LocalStorageManager()

generated_scenarios = [
    {
        "title": "Redact Username Decorator",
        "difficulty": 3,
    "description": "Create a decorator that get a username as a parameter and reducts the username from **ALL** input arguments of the function it decorates by using '???'  \nFor example if the username is  \n```Thomas```  \nand the function is called with  \n```Thomas is tired```  \nit should replace the argument with  \n```??? is tired```",
    "initial_code": "def redact_username(username: str):\n    # Your code here\n    pass",
    "function_name": "test_function",
    "test_setup_code": "@redact_username('John')\ndef test_function(input_string: str, notes: str=\"none\"):\n    return input_string + ' Notes: ' + notes",
    "test_cases": [
        {
            "input": ("John is tired",),
            "expected_output": "??? is tired Notes: none",
            "description": "Redacting username 'John' should return '???'."
        },
        {
            "input": ("Alice and John are buying a house",),
            "expected_output": "Alice and ??? are buying a house Notes: none",
            "description": "Redacting username 'John' should return 'Alice and ??? are buying a house'."
        },
        {
            "input": ("Charlie doesn't know anybody",),
            "expected_output": "Charlie doesn't know anybody Notes: none",
            "description": "No redaction needed as 'Charlie' is not the username."
        },
        {
            "input": ("Bank is closing loan", "John is the manager"),
            "expected_output": "Bank is closing loan Notes: ??? is the manager",
            "description": "All parameters should be redacted if they contain the username."
        },
        {
            "input": {"input_string":"Bank is closing loan", "notes":"John is the manager"},
            "expected_output": "Bank is closing loan Notes: ??? is the manager",
            "description": "All parameters should be redacted if they contain the username."
        }
    ]
},
{
    "title": "Unpacking and Extended Iterable Unpacking",
    "difficulty": 2,
    "description": (
        "Create a function called `split_first_last` that takes a list of at least two elements and returns a tuple "
        "containing the first element, a list of all middle elements, and the last element. "
        "Demonstrate your understanding of iterable unpacking and the use of the * operator in function arguments.\n\n"
        "For example:\n"
        "```python\n"
        "split_first_last([1, 2, 3, 4])  # (1, [2, 3], 4)\n"
        "split_first_last(['a', 'b', 'c'])  # ('a', ['b'], 'c')\n"
        "```\n"
        "If the list has only two elements, the middle list should be empty."
    ),
    "initial_code": (
        "def split_first_last(lst):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "split_first_last",
    "test_cases": [
        {
            "input": ([1, 2, 3, 4],),
            "expected_output": (1, [2, 3], 4),
            "description": "Should return (1, [2, 3], 4) for [1, 2, 3, 4]."
        },
        {
            "input": (['a', 'b', 'c'],),
            "expected_output": ('a', ['b'], 'c'),
            "description": "Should return ('a', ['b'], 'c') for ['a', 'b', 'c']."
        },
        {
            "input": ([10, 20],),
            "expected_output": (10, [], 20),
            "description": "Should return (10, [], 20) for [10, 20]."
        },
        {
            "input": ([1, 2, 3, 4, 5, 6],),
            "expected_output": (1, [2, 3, 4, 5], 6),
            "description": "Should return (1, [2, 3, 4, 5], 6) for [1, 2, 3, 4, 5, 6]."
        }
    ]
},
    {
        "title": "Add two numbers",
        "difficulty": 1,
    "description": "Create a function that adds two numbers together and returns the result.",
    "initial_code": "def add_numbers(a: int, b: int) -> int:\n    # Your code here\n    pass",
    "function_name": "add_numbers",
    "test_cases": [
        {
            "input": (2, 3),
            "expected_output": 5,
            "description": "Adding 2 and 3 should return 5."
        },
        {
            "input": (-1, 1),
            "expected_output": 0,
            "description": "Adding -1 and 1 should return 0."
        },
        {
            "input": (0, 0),
            "expected_output": 0,
            "description": "Adding 0 and 0 should return 0."
        }
    ]
},
    {
        "title": "Reverse list",
        "difficulty": 1,
    "description": "Create a function that reverses a list and returns the reversed list.",
    "initial_code": "def reverse_list(lst: list) -> list:\n    # Your code here\n    pass",
    "function_name": "reverse_list",
    "optional_code_goal": {"max_lines": 1},
    "test_cases": [
        {
            "input": ([2, 3],),
            "expected_output": [3, 2],
            "description": "Reversing the list [2, 3] should return [3, 2]."
        },
        {
            "input": ([5, 4, 3, 2, 1],),
            "expected_output": [1, 2, 3, 4, 5],
            "description": "Reversing the list [5, 4, 3, 2, 1] should return [1, 2, 3, 4, 5]."
        },
        {
            "input": ([1],),
            "expected_output": [1],
            "description": "Reversing the list [1] should return [1]."
        },
        {
            "input": ([],),
            "expected_output": [],
            "description": "Reversing an empty list should return an empty list."
        }

    ]
},
    {
        "title": "Group by Remainder",
        "difficulty": 2,
    "description": "Given a list of integers, create a function that returns a dictionary  that groups the integers based on the remainder when divided  by a given divisor. The keys of the dictionary should be the remainders, and the values should be lists of integers that yield those remainders.",
    "initial_code": "def group_by_remainder(lst:list, divisor:int) -> int:\n    # Your code here\n    pass",
    "function_name": "group_by_remainder",
    "optional_code_goal": {"max_lines": 3},
    "test_cases": [
        {
            "input": ([10, 20, 30, 25, 15], 5),
            "expected_output": {0: [10, 20, 30, 25, 15],},
            "description": "Grouping by remainder when divided by 5."
        },
        {
            "input": ([1, 2, 3, 4, 5], 2),
            "expected_output": {0: [2, 4], 1: [1, 3, 5]},
            "description": "Grouping by remainder when divided by 2."
        },
        {
            "input": ([7, 14, 21], 7),
            "expected_output": {0: [7, 14, 21]},
            "description": "All numbers yield the same remainder when divided by 7."
        },
        {
            "input": ([8, -8, -16], 4),
            "expected_output": {0: [8, -8, -16]},
            "description": "All numbers yield the same remainder when divided by 4."
        }
    ]
    
},
{    "title": "Calculate Factorial",
        "difficulty": 2,
    "description": "Create a function that calculates the factorial of a given number and returns the result.",
    "initial_code": "def factorial(n: int) -> int:\n    # Your code here\n    pass",
    "function_name": "factorial",
    "test_cases": [
        {
            "input": (5,),
            "expected_output": 120,
            "description": "Factorial of 5 should return 120."
        },
        {
            "input": (0,),
            "expected_output": 1,
            "description": "Factorial of 0 should return 1."
        },
        {
            "input": (1,),
            "expected_output": 1,
            "description": "Factorial of 1 should return 1."
        },
        {
            "input": (3,),
            "expected_output": 6,
            "description": "Factorial of 3 should return 6."
        }
    ]
},
{
    "title": "Dictionary Comprehension with Conditional Logic",
    "difficulty": 1,
    "description": (
        "Create a function called `even_square_dict` that takes a list of integers and returns a dictionary where the keys "
        "are the even numbers from the list and the values are their squares. Suggestion: Use a dictionary comprehension with a condition.\n\n"
        "For example:\n"
        "```python\n"
        "even_square_dict([1, 2, 3, 4, 5])  # {2: 4, 4: 16}\n"
        "even_square_dict([10, 15, 20])  # {10: 100, 20: 400}\n"
        "even_square_dict([])  # {}\n"
        "```\n"
        "Demonstrate your understanding of dictionary comprehensions and conditional logic in Python."
    ),
    "initial_code": (
        "def even_square_dict(numbers):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "even_square_dict",
    "test_cases": [
        {
            "input": ([1, 2, 3, 4, 5],),
            "expected_output": {2: 4, 4: 16},
            "description": "Should return {2: 4, 4: 16} for [1, 2, 3, 4, 5]."
        },
        {
            "input": ([10, 15, 20],),
            "expected_output": {10: 100, 20: 400},
            "description": "Should return {10: 100, 20: 400} for [10, 15, 20]."
        },
        {
            "input": ([1, 3, 5],),
            "expected_output": {},
            "description": "Should return {} for [1, 3, 5] (no even numbers)."
        },
        {
            "input": ([],),
            "expected_output": {},
            "description": "Should return {} for an empty list."
        }
    ]
},
{
    "title": "Tuple Packing and Unpacking",
    "difficulty": 2,
    "description": (
        "Create a function called `swap_and_pack` that takes two arguments, swaps them, and returns them as a tuple. "
        "Then, demonstrate tuple unpacking by writing a test that unpacks the result into two variables. "
        "This exercise is to show your understanding of tuple packing and unpacking in Python.\n\n"
        "For example:\n"
        "```python\n"
        "result = swap_and_pack('hello', 42)  # (42, 'hello')\n"
        "a, b = swap_and_pack('hello', 42)\n"
        "# a == 42, b == 'hello'\n"
        "```\n"
        "If you pass two values, the function should return them swapped in a tuple."
    ),
    "initial_code": (
        "def swap_and_pack(a, b):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "swap_and_pack",
    "test_cases": [
        {
            "input": ("hello", 42),
            "expected_output": (42, "hello"),
            "description": "Should return (42, 'hello') for input ('hello', 42)."
        },
        {
            "input": (1, 2),
            "expected_output": (2, 1),
            "description": "Should return (2, 1) for input (1, 2)."
        },
        {
            "input": ([1, 2], {"a": 10}),
            "expected_output": ({"a": 10}, [1, 2]),
            "description": "Should return ({'a': 10}, [1, 2]) for input ([1, 2], {'a': 10})."
        }
    ]
},
{
    "title": "Class Decorator: Add Repr",
    "difficulty": 2,
    "description": (
        "Write a class decorator called `add_repr` that adds a custom `__repr__` method to any class it decorates. "
        "The `__repr__` method should return a string in the format `<ClassName({attribute_dict})>`, "
        "where `attribute_dict` is the dictionary of the instance's attributes.\n\n"
        "For example:\n"
        "```python\n"
        "@add_repr\n"
        "class Point:\n"
        "    def __init__(self, x, y):\n"
        "        self.x = x\n"
        "        self.y = y\n"
        "p = Point(1, 2)\n"
        "repr(p)  # <Point({'x': 1, 'y': 2})>\n"
        "```\n"
        "Demonstrate your understanding of class decorators and dynamic method addition."
    ),
    "initial_code": (
        "def add_repr(cls):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "test_point_repr",
    "test_setup_code": (
        "@add_repr\n"
        "class Point:\n"
        "    def __init__(self, x, y):\n"
        "        self.x = x\n"
        "        self.y = y\n"
        "def test_point_repr():\n"
        "    p = Point(3, 4)\n"
        "    return repr(p)\n"
    ),
    "test_cases": [
        {
            "input": (),
            "expected_output": "<Point({'x': 3, 'y': 4})>",
            "description": "Should return custom repr for Point(3, 4)."
        }
    ]
},
{
    "title": "Function Decorator: Double Result",
    "difficulty": 2,
    "description": (
        "Write a function decorator called `double_result` that, when applied to any function, "
        "will double the result returned by that function. The decorator should not take any arguments.\n\n"
        "For example:\n"
        "```python\n"
        "@double_result\n"
        "def add(a, b):\n"
        "    return a + b\n"
        "add(2, 3)  # 10\n"
        "```\n"
        "Demonstrate your understanding of function decorators in Python."
    ),
    "initial_code": (
        "def double_result(func):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "add",
    "test_setup_code": (
        "@double_result\n"
        "def add(a, b):\n"
        "    return a + b\n"
    ),
    "test_cases": [
        {
            "input": (1,3),
            "expected_output": 8,
            "description": "add(1, 3) should return 8 because the result is doubled."
        },
        {
            "input": (0, 0),
            "expected_output": 0,
            "description": "add(0, 0) should return 0 because the result is doubled."
        },
        {
            "input": (-1, 2),
            "expected_output": 2,
            "description": "add(-1, 2) should return 2 because the result is doubled."
        }
    ]
},

]

st.session_state[FINISHED_KEY] = localS.getItem(FINISHED_KEY) or {}

scenarios = sorted(generated_scenarios, key=lambda x: x["difficulty"])

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