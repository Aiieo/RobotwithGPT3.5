import os
import openai
from action import *

openai.api_key = "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"

messages = [{"role":"system","content":"你是一个餐厅服务员机器人，当发起会话的时候你需要询问客人是否需要帮助。"}]
while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    functions = [
    {
        "name":"take_order",
        "description":"顾客点餐",
        "parameters":{
            "type":"object",
            "properties":{},
        },
    },
    {
        "name":"menu_suggestion",
        "description":"给顾客点餐建议",
        "parameters":{
            "type":"object",
            "properties":{},
            
        },
    },
    {
        "name":"special_diet",
        "description":"询问顾客是否有忌口",
        "parameters":{
            "type":"object",
            "properties":{},

        },
    },
    {
        "name":"billing",
        "description":"确认顾客是否需要结帐",
        "parameters":{
            "type":"object",
            "properties":{},

        },
    },
    {
        "name":"service_explanation",
        "description":"告诉顾客餐厅服务员机器人能提供的服务",
        "parameters":{
            "type":"object",
            "properties":{},

        },
    },
        {
        "name":"go_kitchen",
        "description":"前往厨房",
        "parameters":{
            "type":"object",
            "properties":{},

        },
    },    {
        "name":"make",
        "description":"做菜",
        "parameters":{
            "type":"object",
            "properties":{},

        },
    },    {
        "name":"serve",
        "description":"当做好菜后把菜段给顾客",
        "parameters":{
            "type":"object",
            "properties":{},

        },
    },
]
    print(messages)
    print("***************************\n")
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0613",
      messages=messages,
      functions = functions,
      function_call="auto",
      temperature=0,
    )
    print(completion)
    response_message = completion
    answer = response_message.choices[0].message.content
    
    print("*********************")
    funcall = response_message.choices[0].message.get("function_call")
    # print("本次回应的function_call为:"+funcall)
    print("*********************")

    if response_message.choices[0].message.get("function_call"):
        print("进入function_call")
        available_functions = {
            "greeting":greeting,
            "take_order":take_order,
            "menu_suggestion":menu_suggestion,
            "special_diet":special_diet,
            "service_explanation":service_explanation,
            "billing":billing,
            "go_kitchen":go_kitchen,
            "make":make,
            "serve":serve,
        } 

        function_name = funcall["name"]
        fuction_to_call = available_functions[function_name]

        print("**********************funcall********************")
        print(funcall)
        print("arguments:"+funcall["arguments"])
        print("**********************funcall********************")

        function_args = funcall["arguments"]
        function_response = fuction_to_call()
        
        print(json.loads(function_response)['contents']+"***")

        #messages.append(response_message)  
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": json.loads(function_response)['contents'],
            }
        )  
        print("****************message****************")
        print(messages)
        print("****************second_response****************")
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  
        print("****************second_response_end****************")
        print(second_response)
        answer = second_response['choices'][0]['message'].get("content")
    #print(completion['choices'][0]['message']['function_call']['name'])
    print(f'ChatGPT: {answer}')
    messages.append({"role": "assistant", "content": answer})
