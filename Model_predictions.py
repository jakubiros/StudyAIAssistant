import ollama

class OllamaAgent:
    def __init__(self, model_version: str = 'smollm2:1.7b'):
        self.model_version=model_version

    def run(self, prompt):
        response = ollama.chat(model=self.model_version, messages=prompt.get_messages())
        return response['message']['content']

class BasePrompt:
    def __init__(self, text:str):
        self.text=text

    def get_messages(self):
        return [{'role':'user', 'content': self.text}]


class SummaryPrompt(BasePrompt):
        def get_messages(self):
            return [
                {'role': 'system', 'content': 'Summarize and extract useful content'},
                {'role': 'user', 'content': self.text}
            ]

class KeyPrompt(BasePrompt):
    def get_messages(self):
        return [
            {'role': 'system', 'content': 'Extract key points'},
            {'role': 'user', 'content': self.text}
        ]

class ContextPrompt:
    def __init__(self, text:str, user_question:str):
        self.text=text
        self.user_question=user_question
    def get_messages(self):
        return [
            {'role': 'system', 'content': f'You are a helpful educational assistant. Answer user questions about notes. If the information is nott in the text be clear about it.'
                                          f'\n\n--- BRGINING OF NOTE ---\n{self.text}\n--- END OF NOTE ---'},
            {'role': 'user', 'content': self.user_question}
        ]