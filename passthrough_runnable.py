from config import ENV_CONFIG
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough

# Model
model = ChatMistralAI(model=ENV_CONFIG.MISTRAL_AI_MODEL)

# Output parser
parser = StrOutputParser()

code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator in python"),
    ("human", "{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explain code in terms"),
    ("human", "Explain the folloeing code in simple words:\n {code} ")
])

# Here we have pass the response of the generate_code to the explain_Code
# sequence = code_prompt | model | parser | explain_prompt | model | parser

# result = sequence.invoke({"topic":"Write a code to search target element in the rotated sorted array in python."})

# print(result)

# in result we dont have any kind of code only have to explaination

# we have not saved code between passing to the parser | explain_prompt

seq1 = code_prompt | model | parser

seq2 = RunnableParallel({
    "code": RunnablePassthrough(),
    "explanation": RunnableLambda(lambda x: {"code": x}) | explain_prompt | model | parser
})

runnable = seq1 | seq2

result = runnable.invoke({"topic": "Write a code to search target element in the rotated sorted array in python."})

print(result["code"])
print(result["explanation"])

# print(result)