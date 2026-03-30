import fitz
import io

class DocumentReader:
    @staticmethod
    def extract_text_pdf(file_bytes):
        text=''
        try:
            doc=fitz.open(stream=file_bytes, filetype="pdf")
            for page in doc:
                text +=page.get_text() + '\n'
            return text
        except Exception as e:
            #st.error
            return ''