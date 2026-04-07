from config import ENV_CONFIG
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

search_tool = TavilySearchResults(max_result=5)

llm = ChatMistralAI(model=ENV_CONFIG.MISTRAL_AI_MODEL)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful AI assistant

    summarize the following news into clear bullet points

    {news}
"""
)

chain = prompt | llm | parser

news_result = search_tool.run("Latest AI news in india in April 2026")

result = chain.invoke({"news": news_result})

print(result)