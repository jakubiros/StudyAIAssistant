import streamlit as st
from DataProcessing import DocumentReader
from Model_predictions import OllamaAgent, ContextPrompt

def get_agent():
    return OllamaAgent()

def main():
    st.set_page_config(page_title="AI Asystent", page_icon="🎓", layout="centered")

    agent = get_agent()

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "context_text" not in st.session_state:
        st.session_state.context_text = ""

    col1,col2=st.columns([4,1])
    with col1:
        st.title('Your AI Assistant')
    with col2:
        if st.button('Clear Chat', use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    with st.expander('Manage education materials (Click, to expand)', expanded=not bool(st.session_state.context_text)):
        tab_text,tab_pdf=st.tabs(['Paste text', 'Upload PDF'])


if __name__ == "__main__":
    main()