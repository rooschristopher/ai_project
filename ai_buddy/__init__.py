import openai
import os
import json
import dotenv
import requests
from googleapiclient.discovery import build # pip install google-api-python-client


dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")
google_api_key = os.getenv("GOOGLE_API_KEY")
cse_id = os.getenv("CSE_ID")

models = [x['id'] for x in openai.Model.list()['data']]


class Agent:
    def __init__(self, directory=None, model='gpt-3.5-turbo-0301'):
        self.history = []
        self.actions = []
        self.action_history = []
        self.directory = directory
        self.model = model

    def chat(self, prompt, prompt_template=None):
        if prompt_template:
            prompt = prompt_template.transform(prompt)
        message = {"role": "user", "content": prompt}
        self.history.append(message)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.history)
        message = response["choices"][0]["message"]
        self.history.append(message)
        return message


    def get_webpage(self, url):
        r = requests.get(url)
        return r.text

    def google_search(self, search_term, **kwargs):
        service = build("customsearch", "v1", developerKey=google_api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res

    def write_to_file(self):
        pass

    def run_file(self):
        pass









class PromptTemplate:
    def __init__(self, prompt_function):
        self.


# class Agent:
#     def __init__(self, prompt_template: str = "default", model: str = "gpt-3.5-turbo-0301", ) -> None:
#         if prompt_template in templates.keys():
#             self.prompt_template = prompt_template
#             self.start = templates[prompt_template]["start"]
#             self.end = templates[prompt_template]["end"]
#
#         else:
#             raise Exception("Invalid prompt template")
#         self.prompt_template = prompt_template
#         if model in models:
#             self.model = model
#         else:
#             raise Exception("Invalid model")
#
#         self.session_memory = []
#
#
#     def set_prompt_template(self, prompt_template: str) -> None:
#         self.prompt_template = prompt_template
#
#     def complete_text(self, prompt, max_tokens: int = 100, n=1):
#         response = openai.Completion.create(
#             engine=self.model,
#             prompt=self.start + " " + prompt + " " + self.end,
#             max_tokens=max_tokens,
#             n=n,
#             stop=None,
#             temperature=1,
#         )
#         completions = [choice.text.strip() for choice in response.choices]
#         return completions
#
#     def complete_chat(self, prompt, max_tokens: int = 100, n=1):
#
#         message = {"role": "user", "content": self.start + " " + prompt + " " + self.end}
#         self.session_memory.append(message)
#         response = openai.ChatCompletion.create(
#             model=self.model,
#             messages=self.session_memory
#         )
#         message = response["choices"][0]["message"]
#         self.session_memory.append(message)
#
#         return message
#
# class Message:
#     def __init__(self, sender: str, receivers: list, message: str) -> None:
#         self.sender = sender
#         self.receivers = receivers
#         self.message = message
#
#
# if __name__ == "__main__":
#     # agent = Agent()
#     # r = agent.complete_chat("Hello world")
#     python_agent = Agent(prompt_template="python_code", model="gpt-3.5-turbo-0301")
#     r = python_agent.complete_chat("Write a python script that gets the current time and date and prints it to the console.")
#     # write to file
#     with open("output.py", "w") as f:
#         f.write(r)
#
#
#






