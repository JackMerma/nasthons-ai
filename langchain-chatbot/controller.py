import os
from langchain_community.chat_models.ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate


def build_respose(context, query):

    messages = template_from_messages(query)
    prompt_template = ChatPromptTemplate.from_messages(messages)
    prompt = prompt_template.invoke({""})

    llm_model = ChatOllama(model=os.getenv('LLM_MODEL'), temperature=0.1)

    return llm_model.invoke(prompt)
