import streamlit as st
import os
from streamlit_local_storage import LocalStorage

st.set_page_config(
    page_title="Python | Lectures",
    initial_sidebar_state="expanded",
    page_icon=":snake:",
    layout="wide",
)

PROGRESS_KEY = 'lecture_progress'
FINISHED_KEY = 'lecture_finished'
def LocalStorageManager():
    return LocalStorage()
localS = LocalStorageManager()



def __get_lecture_id(lecture_name):
    return lecture_name[4:-3]

script_dir = os.path.dirname(os.path.abspath(__file__))
materials_dir = os.path.join(script_dir, '..','materials')
lecture_list = sorted(os.listdir(materials_dir))

st.session_state[PROGRESS_KEY] = localS.getItem(PROGRESS_KEY) or lecture_list[0]
st.session_state[FINISHED_KEY] = localS.getItem(FINISHED_KEY) or []

def get_current_lecture():
    stored_progress = st.session_state[PROGRESS_KEY] or []
    if stored_progress:
        return next((lec for lec in lecture_list if __get_lecture_id(lec) == stored_progress), lecture_list[0])

def update_progress(lecture_name):
    lecture_id = __get_lecture_id(lecture_name)
    localS.setItem(PROGRESS_KEY, lecture_id)
    st.session_state[PROGRESS_KEY] = lecture_id

def toggle_lecture_done(lecture_name):
    finished = st.session_state[FINISHED_KEY] or []
    lecture_id = __get_lecture_id(lecture_name)
    if lecture_id in finished:
        finished.remove(lecture_id)
    else:
        finished.append(lecture_id)
    localS.setItem(FINISHED_KEY, finished)
    st.session_state[FINISHED_KEY] = finished

def is_any_lecture_done():
    return bool(st.session_state[FINISHED_KEY] or [])

def is_lecture_done(lecture_name):
    return __get_lecture_id(lecture_name) in (st.session_state[FINISHED_KEY] or [])

def is_first_lecture():
    return get_current_lecture() == lecture_list[0]

def is_last_lecture():
    return get_current_lecture() == lecture_list[-1]

current_lecture = get_current_lecture().split('.')[0].split('_', maxsplit=2)[1]

with open(os.path.join(materials_dir, get_current_lecture()), 'r') as f:
    content = f.read()
    col1, col2 = st.columns(2)

    st.checkbox("Mark complete", key="toggle_lecture", value=is_lecture_done(get_current_lecture()), on_change=lambda: toggle_lecture_done(get_current_lecture()))
    with col1:
        st.button(
            "Previous Lecture",
            type='secondary',
            icon="◀️",
            use_container_width=True,
            key="previous_lecture",
            disabled=is_first_lecture(),
            on_click=lambda: update_progress(lecture_list[(lecture_list.index(get_current_lecture()) - 1) % len(lecture_list)])
        )
    with col2:
        st.button(
            "Next Lecture",
            type='secondary',
            icon="▶️",
            use_container_width=True,
            key="next_lecture",
            disabled=is_last_lecture(),
            on_click=lambda: update_progress(lecture_list[(lecture_list.index(get_current_lecture()) + 1) % len(lecture_list)])
        )
    st.markdown(content)
    

def switch_lecture(lecture_name):
    update_progress(lecture_name)

with st.sidebar:
    st.button("Reset Progress", on_click=lambda: localS.setItem(FINISHED_KEY, []), disabled=not is_any_lecture_done())
    st.title(f"Lectures ({len(lecture_list)} / {len(localS.getItem(FINISHED_KEY) or [])} completed)")
    for lecture in lecture_list:
        lecture_name = lecture.split('.')[0].split('_', maxsplit=1)[1].replace('_', ' ')
        is_done = is_lecture_done(lecture)
        st.button(
            lecture_name,
            use_container_width=True,
            type='primary' if lecture == get_current_lecture() else 'secondary',
            icon="✅" if is_done else "▶️",
            key=lecture,
            on_click=lambda lec=lecture: switch_lecture(lec)
        )