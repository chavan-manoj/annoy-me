import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class LLM:
    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI(model_name=os.getenv("MODEL_NAME"), temperature=0)

    def query(self, system_prompt: str, user_prompt: str, input: dict = {}) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", user_prompt)
        ])
        chain = prompt | self.llm
        response = chain.invoke(input).content
        return response
