import streamlit as st

st.set_page_config(
    page_title="Python | Feedback",
    initial_sidebar_state="expanded",
    page_icon=":snake:",
    layout="wide",
)

st.title("Feedback Page")
st.markdown(
    """
    ### Feedback Form
    Please provide your feedback on the Python FastSkilling platform.
    Your input is valuable to us and will help improve the learning experience.
    """
)
feedback_topic = st.radio(
    "What your feedback is about?",
    ["General Feedback", "Feature request", "Bug Report"],
)

if feedback_topic:
    text = st.text_area(
        "Please provide your feedback here:",
        placeholder="Type your feedback here...",
        height=200,
        max_chars=1000,
        key="feedback_text_area",
    )
    st.markdown(
        """
        **Note**: Please keep your feedback concise and relevant to the topic selected.  
        Once ready, click the 'Create' button to redirect to GitHub where you can finalize your request.
        """
    )
    st.link_button("Create", f"https://github.com/Zolikon/python-fastskilling/issues/new?title={feedback_topic}&body={text}",)