from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# llm=HuggingFaceEndpoint(repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation')

# model= ChatHuggingFace(llm=llm)

model=ChatOpenAI()

template1=PromptTemplate(template="Write a detailed report {topic}",input_variables=['topic'])

template2=PromptTemplate(template="Write a 5 line summary on the following text./n {text}",input_variables=['text'])

parser = StrOutputParser()

chain = template1 | model| parser | template2 | model | parser

result1=chain.invoke({'topic':'black hole'})


print(result1)


