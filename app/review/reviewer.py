from langchain_openai import ChatOpenAI
from app.utils.constants import OpenAIModels, RESUME_REVIEW_PROMPT
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "{RESUME_REVIEW_PROMPT}"),
    ("user", "{resume_text}")
])

llm = ChatOpenAI(model_name=OpenAIModels.GPT4_TURBO.value)

chain = prompt | llm | output_parser


def analyze_resume(resume_text: str) -> str:
    return chain.invoke({
        "resume_text": resume_text,
        "RESUME_REVIEW_PROMPT": RESUME_REVIEW_PROMPT
    })

