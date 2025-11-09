from langchain_community.tools import DuckDuckGoSearchRun,ShellTool
from langchain_core.tools import tool,StructuredTool,BaseTool
from pydantic import BaseModel,Field
from typing import Type

# builtin- tools
search_tool=DuckDuckGoSearchRun()

results = search_tool.invoke("what is ipl?")
# print(results)

# Shell tool

shell_tool=ShellTool()

result = shell_tool.invoke('ls')
# print(result)

# our own tool

## Method-1 (mostly used)
@tool
def multiply(a,b):
    """ Multiply two numbers"""
    return a*b


result=multiply.invoke({"a":3,"b":5})
# print(result)
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

#Method-2
class MultiplyInput(BaseModel):
    a:int =Field(required=True,description="The first number to multiply")
    b:int =Field(required=True,description="The second number to multiply")

def multiply_func(a:int,b:int)->int:
    return a*b

multiply_tool= StructuredTool.from_function(func=multiply_func,name="multiply"
                                            ,description="Multiply two number"
                                            ,args_schema=MultiplyInput)

result=multiply.invoke({"a":3,"b":5})
# print(result)

#Method-3
class MultTool(BaseTool):
    name:str="multiply"
    description:str="Multiply two numbers"
    args_schema:Type[BaseModel]=MultiplyInput
    
    def _run(self,a:int,b:int)->int:
        return a*b
    
mult_tool=MultTool()

result=multiply.invoke({"a":3,"b":5})
# print(result)
