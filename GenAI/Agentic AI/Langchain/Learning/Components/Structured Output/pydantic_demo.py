from pydantic import BaseModel,Field
from typing import Optional

class Student (BaseModel):
    name :str ='Divyanshu'
    age:Optional[int]=None 
    cgpa:float=Field(gt=0,lt=10,default=5,description='A decimal number respresenting the student cgpa')

# newStudent ={'name':'Divyanshu'}

student =Student()
print(student)