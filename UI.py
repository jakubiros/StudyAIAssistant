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

        with tab_text:
            user_text=st.text_area('Paste notes:', height=350, placeholder='Copy and paste your text here...')
            if st.button('Save text'):
                if user_text.strip():
                    st.session_state.context_text = user_text
                    st.session_state.messages = []
                    st.success('Notes saved! You can use chat. ')
                else:
                    st.warning('Area is empty.')

        with tab_pdf:
            uploaded_file=st.file_uploader('Drag and drop PDF file', type='pdf')
            if uploaded_file:
                if st.button('Load PDF'):
                    with st.spinner('PDF Processing...'):
                        extracted_text=DocumentReader.extract_text_pdf(uploaded_file.read())
                        st.session_state.context_text = extracted_text
                        st.session_state.messages = []
                    st.success(f'Loaded {uploaded_file.name}')

if __name__ == "__main__":
    main()