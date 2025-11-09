from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Sentiment(BaseModel):
    sentiment:Literal["positive","negative"] =Field(description="Give sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Sentiment)

prompt1= PromptTemplate(template="Classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}",
                        input_variables=["feedback"],
                        partial_variables={'format_instruction':parser2.get_format_instructions()})

classifer_chain= prompt1| model | parser2

prompt2=PromptTemplate(template="Write a appropriate repsonse for the following positve feedback \n {feedback}",input_variables=["feedback"])
prompt3=PromptTemplate(template="Write a appropriate repsonse for the following negative feedback \n {feedback}",input_variables=["feedback"])

conditional_branch=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2 | model| parser ),
    (lambda x:x.sentiment=='negative',prompt3 | model | parser),
    RunnableLambda(lambda x:"Could not find the sentiment")
)

chain=classifer_chain | conditional_branch

result = chain.invoke({'feedback': 'This is a best phone.'})
print(result)
