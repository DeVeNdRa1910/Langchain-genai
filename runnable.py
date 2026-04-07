from config import ENV_CONFIG

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt Tmeplate
prompt = ChatPromptTemplate.from_template(
    "You are a Bhojpuri language expert. Explain {topic} in simple Bhojpuri."
)

# Model
model = ChatMistralAI(model=ENV_CONFIG.MISTRAL_AI_MODEL)

# Output parser
parser = StrOutputParser()

runnable = prompt | model | parser

# Invoke the chain
response = runnable.invoke({"topic": "Langchain"})

print(response)