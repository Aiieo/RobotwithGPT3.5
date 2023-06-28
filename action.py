import json

def greeting():
    greeting_info = {
        "action":"greeting",
        "message":"欢迎光临！您好，我是餐厅服务员机器人。有什么我可以帮您的吗？"
    }
    return json.dumps(greeting_info)

def take_order():
    take_order_info = {
      "action": "take_order",
      "contents": "请告诉我您的点菜内容，我会尽快为您下单。"
    }
    return json.dumps(take_order_info)

def menu_suggestion():
    menu_suggestion_info = {
      "action": "menu_suggestion",
      "contents": "您可以尝试我们的特色菜，比如烤鸭和红烧狮子头。"
    }
    return json.dumps(menu_suggestion)

def special_diet():
    special_diet_info = {
      "action": "special_diet",
      "contents": "如果您有任何饮食限制或过敏，请告诉我，我们将为您提供合适的选择。"
    }
    return json.dumps(special_diet_info)

def service_explanation():
    service_explanation_info = {
      "action": "service_explanation",
      "contents": "我们的服务包括点菜、上菜、饮料服务等。如果您有其他需求，请随时告诉我。"
    }
    return json.dumps(service_explanation_info)

def billing():
    billing_info = {
      "action": "billing",
      "contents": "请问您需要结账了吗？我们接受现金和信用卡付款。"
    }
    return json.dumps(billing_info)