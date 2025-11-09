from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool,InjectedToolArg
from typing import Annotated
from dotenv import load_dotenv

load_dotenv()


currency_rates_inr = {
    "INR": 1.0,       # Indian Rupee
    "USD": 0.012,     # United States Dollar
    "EUR": 0.011,     # Euro
    "GBP": 0.0098,    # British Pound
    "JPY": 1.80,      # Japanese Yen
    "CNY": 0.087,     # Chinese Yuan
    "AUD": 0.019,     # Australian Dollar
    "CAD": 0.016,     # Canadian Dollar
    "CHF": 0.011,     # Swiss Franc
    "SGD": 0.016      # Singapore Dollar
}

@tool
def get_conversion_factor(base_curr:str,target_curr:str)->float:
     """
    Returns how many units of 'to_curr' equal 1 unit of 'from_curr'.
    Rates are internally based on INR.
    """
     conv_rate= currency_rates_inr[target_curr]/currency_rates_inr[base_curr] 
     return conv_rate

@tool
def convert_curr (base_curr_val:int , conv_rate:Annotated[float,InjectedToolArg])->float:
      """Given a currency conversion rate this function calculate the target currency value from a given base currency value"""
      return base_curr_val * conv_rate

llm=ChatOpenAI()

llm_with_tools=llm.bind_tools([get_conversion_factor,convert_curr])

messages=[HumanMessage("What is the conversion factor between USD and INR and based on that can you convert 10 USD to INR.")]



# for tool_call in ai_message.tool_calls:
#       if tool_call['name']=='get_conversion_factor':
#             tool_message1=get_conversion_factor.invoke(tool_call)
#             conv_rate=tool_message1.content
#             messages.append(tool_message1)
#       if tool_call['name']=='convert_curr':
#             tool_call['args']['conv_rate']=conv_rate
#             tool_message2=convert_curr.invoke(tool_call)
#             messages.append(tool_message2)


conv_rate=1
while True:
    ai_message=llm_with_tools.invoke(messages)
    messages.append(ai_message)

    if not ai_message.tool_calls:
          break

    for tool_call in ai_message.tool_calls:
        if tool_call['name']=='get_conversion_factor':
                tool_message1=get_conversion_factor.invoke(tool_call)
                conv_rate=tool_message1.content
                messages.append(tool_message1)
        if tool_call['name']=='convert_curr':
                tool_call['args']['conv_rate']=conv_rate
                tool_message2=convert_curr.invoke(tool_call)
                messages.append(tool_message2)

print(llm_with_tools.invoke(messages))


# print(messages)