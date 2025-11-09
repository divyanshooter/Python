from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(repo_id='google/gemma-2-2b-it',
    task='text-generation')

model = ChatHuggingFace(llm=llm)

parser =StrOutputParser()

template = PromptTemplate(template ="Generate 5 interseting facts about the {topic}",input_variables=['topic'])

chain= template | model | parser
result = chain.invoke({'topic':'Black hole'})

print(result)

chain.get_graph().print_ascii()