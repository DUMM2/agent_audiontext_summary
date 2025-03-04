import openai as ai
import os

class LLM:
    def __init__(self, model='gpt-3.5-turbo'):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = model


    def chat(self, prompt, max_tokens=50):
        response = ai.chat.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=max_tokens,
            api_key=self.api_key
        )
        return response.choices[0].text.strip()