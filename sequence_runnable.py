from config import ENV_CONFIG

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Model
model = ChatMistralAI(model=ENV_CONFIG.MISTRAL_AI_MODEL)

# Parser
parser = StrOutputParser()

# Step 1: Generate roadmap
roadmap_prompt = ChatPromptTemplate.from_template(
    "Generate a 12-month roadmap to master {topic}"
)

# Step 2: Pick one key topic from roadmap
extract_prompt = ChatPromptTemplate.from_template(
    "From the following roadmap, extract one important topic:\n{roadmap}"
)

# Step 3: Explain that topic
explain_prompt = ChatPromptTemplate.from_template(
    "Explain this topic in detail:\n{extracted_topic}"
)

# Sequential chain
chain = (
    {
        "roadmap": roadmap_prompt | model | parser
    }
    | extract_prompt
    | model
    | parser
    | (lambda extracted_topic: {"extracted_topic": extracted_topic})
    | explain_prompt
    | model
    | parser
)

# OR

or_chain = (
    roadmap_prompt
    | model
    | parser
    | (lambda roadmap: {"roadmap": roadmap})
    | extract_prompt
    | model
    | parser
    | (lambda topic: {"extracted_topic": topic})
    | explain_prompt
    | model
    | parser
)

# Run
result = chain.invoke({"topic": "Machine Learning"})

print(result)



(lambda extracted_topic: {"extracted_topic": extracted_topic})