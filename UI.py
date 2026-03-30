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


if __name__ == "__main__":
    main()