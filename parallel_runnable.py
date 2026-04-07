from config import ENV_CONFIG

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

# Model
model = ChatMistralAI(model=ENV_CONFIG.MISTRAL_AI_MODEL)

# Output parser
parser = StrOutputParser()

short_prompts = ChatPromptTemplate.from_messages(
    [
        ("human", "Generate the roadmap to master {topic} in 12 months"),
    ]
)

detailed_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "Explain the {agenda} in detaile")
    ]
)

topic = "Machine Learning"
agenda = "Langchain"


runnables = RunnableParallel({
    "short_chain": RunnableLambda(lambda x: x["short_chain"]) | short_prompts | model | parser,
    "detail_chain": RunnableLambda(lambda x: x["detail_chain"]) | detailed_prompt | model | parser
})

result = runnables.invoke({
    "short_chain": {"topic": "Machine Learning"},
    "detail_chain": {"agenda": "Deep Learning"}
})

print(result["short_chain"])
print(result["detail_chain"])