import os
import openai
from restaurantRob.action import *

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role":"system","content":"你是一个餐厅服务员机器人，当发起会话的时候你需要询问客人是否需要帮助"}]
while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0613",
      messages=messages,
      functions = functions,
      function_call="auto",
      temperature=1,
    )
    print(completion)
    response_message = completion
    answer = response_message.choices[0].message.content
    
    if response_message.get("function_call"):
        available_functions = {
            "greeting":greeting,
            "take_order":take_order,
            "menu_suggestion":menu_suggestion,
            "special_diet":special_diet,
            "service_explanation":service_explanation,
            "billing":billing,
        } 

        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        # function_args = json.loads(response_message["function_call"]["arguments"])
        # function_response = fuction_to_call(
        #     # action=function_args.get("action"),
        #     # contents=function_args.get("contents"),
        # )

        # print(response_message+"************")
       
        messages.append(response_message)  
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": fuction_to_call["contents"],
            }
        )  

        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,

        )  
        answer = second_response
    print(f'ChatGPT: {answer}')
    messages.append({"role": "assistant", "content": answer})
