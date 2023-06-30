# import json

# def close(arg1):
#     close_info = {
#         "action": "close",
#         "contents": "关闭" + arg1
#     }
#     return json.dumps(close_info)

# def cut(arg1):
#     cut_info = {
#         "action": "cut",
#         "contents": "切割" + arg1
#     }
#     return json.dumps(cut_info)

# def drop(arg1):
#     drop_info = {
#         "action": "drop",
#         "contents": "放下" + arg1
#     }
#     return json.dumps(drop_info)

# def find(arg1):
#     find_info = {
#         "action": "find",
#         "contents": "找到" + arg1
#     }
#     return json.dumps(find_info)

# def grab(arg1):
#     grab_info = {
#         "action": "grab",
#         "contents": "抓住" + arg1
#     }
#     return json.dumps(grab_info)

# def move(arg1):
#     move_info = {
#         "action": "move",
#         "contents": "移动" + arg1
#     }
#     return json.dumps(move_info)

# def open_action(arg1):
#     open_info = {
#         "action": "open",
#         "contents": "打开" + arg1
#     }
#     return json.dumps(open_info)

# def plug_in(arg1):
#     plug_in_info = {
#         "action": "plug in",
#         "contents": "插入" + arg1
#     }
#     return json.dumps(plug_in_info)

# def plug_out(arg1):
#     plug_out_info = {
#         "action": "plug out",
#         "contents": "拔出" + arg1
#     }
#     return json.dumps(plug_out_info)

# def pour(arg1):
#     pour_info = {
#         "action": "pour",
#         "contents": "倒入" + arg1
#     }
#     return json.dumps(pour_info)

# def pull(arg1):
#     pull_info = {
#         "action": "pull",
#         "contents": "拉" + arg1
#     }
#     return json.dumps(pull_info)

# def push(arg1):
#     push_info = {
#         "action": "push",
#         "contents": "推" + arg1
#     }
#     return json.dumps(push_info)

# def put_on(arg1):
#     put_on_info = {
#         "action": "put on",
#         "contents": "穿上" + arg1
#     }
#     return json.dumps(put_on_info)

# def put_in(arg1):
#     put_in_info = {
#         "action": "put in",
#         "contents": "放入" + arg1
#     }
#     return json.dumps(put_in_info)

# def put_back(arg1):
#     put_back_info = {
#         "action": "put back",
#         "contents": "放回" + arg1
#     }
#     return json.dumps(put_back_info)

# def take_off(arg1):
#     take_off_info = {
#         "action": "take off",
#         "contents": "脱下" + arg1
#     }
#     return json.dumps(take_off_info)

# def release(arg1):
#     release_info = {
#         "action": "release",
#         "contents": "释放" + arg1
#     }
#     return json.dumps(release_info)

# def rinse(arg1):
#     rinse_info = {
#         "action": "rinse",
#         "contents": "冲洗" + arg1
#     }
#     return json.dumps(rinse_info)

# def run_to(arg1):
#     run_to_info = {
#         "action": "run to",
#         "contents": "跑到" + arg1
#     }
#     return json.dumps(run_to_info)

# def scrub(arg1):
#     scrub_info = {
#         "action": "scrub",
#         "contents": "擦洗" + arg1
#     }
#     return json.dumps(scrub_info)

# def squeeze(arg1):
#     squeeze_info = {
#         "action": "squeeze",
#         "contents": "挤压" + arg1
#     }
#     return json.dumps(squeeze_info)

# def switch_off(arg1):
#     switch_off_info = {
#         "action": "switch off",
#         "contents": "关闭" + arg1
#     }
#     return json.dumps(switch_off_info)

# def switch_on(arg1):
#     switch_on_info = {
#         "action": "switch on",
#         "contents": "打开" + arg1
#     }
#     return json.dumps(switch_on_info)

# def touch(arg1):
#     touch_info = {
#         "action": "touch",
#         "contents": "触摸" + arg1
#     }
#     return json.dumps(touch_info)

# def turn_to(arg1):
#     turn_to_info = {
#         "action": "turn to",
#         "contents": "转到" + arg1
#     }
#     return json.dumps(turn_to_info)

# def type_on(arg1):
#     type_on_info = {
#         "action": "type on",
#         "contents": "输入" + arg1
#     }
#     return json.dumps(type_on_info)

# def walk_to(arg1):
#     walk_to_info = {
#         "action": "walk to",
#         "contents": "走到" + arg1
#     }
#     return json.dumps(walk_to_info)

# def wash(arg1):
#     wash_info = {
#         "action": "wash",
#         "contents": "清洗" + arg1
#     }
#     return json.dumps(wash_info)

# def wipe(arg1):
#     wipe_info = {
#         "action": "wipe",
#         "contents": "擦拭" + arg1
#     }
#     return json.dumps(wipe_info)

# def stir(arg1):
#     stir_info = {
#         "action": "stir",
#         "contents": "搅拌" + arg1
#     }
#     return json.dumps(stir_info)

# def sweep(arg1):
#     sweep_info = {
#         "action": "sweep",
#         "contents": "扫除" + arg1
#     }
#     return json.dumps(sweep_info)

# def scoop(arg1):
#     scoop_info = {
#         "action": "scoop",
#         "contents": "舀取" + arg1
#     }
#     return json.dumps(scoop_info)

# def lift(arg1):
#     lift_info = {
#         "action": "lift",
#         "contents": "抬起" + arg1
#     }
#     return json.dumps(lift_info)

# def dry(arg1):
#     dry_info = {
#         "action": "dry",
#         "contents": "干燥" + arg1
#     }
#     return json.dumps(dry_info)

# def hang(arg1):
#     hang_info = {
#         "action": "hang",
#         "contents": "挂" + arg1
#     }
#     return json.dumps(hang_info)

# def soak(arg1):
#     soak_info = {
#         "action": "soak",
#         "contents": "浸泡" + arg1
#     }
#     return json.dumps(soak_info)

# def cover(arg1):
#     cover_info = {
#         "action": "cover",
#         "contents": "覆盖" + arg1
#     }
#     return json.dumps(cover_info)

# def uncover(arg1):
#     uncover_info = {
#         "action": "uncover",
#         "contents": "揭开" + arg1
#     }
#     return json.dumps(uncover_info)

# def flip(arg1):
#     flip_info = {
#         "action": "flip",
#         "contents": "翻转" + arg1
#     }
#     return json.dumps(flip_info)

# def screw(arg1):
#     screw_info = {
#         "action": "screw",
#         "contents": "拧紧" + arg1
#     }
#     return json.dumps(screw_info)

# def stretch(arg1):
#     stretch_info = {
#         "action": "stretch",
#         "contents": "拉伸" + arg1
#     }
#     return json.dumps(stretch_info)

# def press(arg1):
#     press_info = {
#         "action": "press",
#         "contents": "按压" + arg1
#     }
#     return json.dumps(press_info)

# def hold(arg1):
#     hold_info = {
#         "action": "hold",
#         "contents": "握住" + arg1
#     }
#     return json.dumps(hold_info)


import json

def greeting():
    print("正在执行"+__name__)
    greeting_info = {
        "action":"greeting",
        "contents":"欢迎光临！您好，我是餐厅服务员机器人。有什么我可以帮您的吗？"
    }
    return json.dumps(greeting_info)

def take_order():
    print("正在执行"+__name__)
    take_order_info = {
      "action": "take_order",
      "contents": "请告诉我您的点菜内容，我会尽快为您下单。"
    }
    return json.dumps(take_order_info)

def menu_suggestion():
    print("正在执行"+__name__)
    menu_suggestion_info = {
      "action": "menu_suggestion",
      "contents": "您可以尝试我们的特色菜，比如烤鸭和红烧狮子头。"
    }
    return json.dumps(menu_suggestion_info)

def special_diet():
    print("正在执行"+__name__)
    special_diet_info = {
      "action": "special_diet",
      "contents": "如果您有任何饮食限制或过敏，请告诉我，我们将为您提供合适的选择。"
    }
    return json.dumps(special_diet_info)

def service_explanation():
    print("正在执行"+__name__)
    service_explanation_info = {
      "action": "service_explanation",
      "contents": "我们的服务包括点菜、上菜、饮料服务等。如果您有其他需求，请随时告诉我。"
    }
    return json.dumps(service_explanation_info)

def billing():
    print("正在执行"+__name__)
    billing_info = {
      "action": "billing",
      "contents": "请问您需要结账了吗？我们接受现金和信用卡付款。"
    }
    return json.dumps(billing_info)

def go_kitchen():
    print("正在执行"+__name__)
    go_kitchen_info = {
      "action": "go_kitchen",
      "contents": "正在导航前往厨房"
    }
    return json.dumps(go_kitchen_info)

def make():
    print("正在执行"+__name__)
    make_info = {
        "actions":"make",
        "contents":"正在制作"
    }
    return json.dumps(make_info)

def serve():
    print("正在执行"+__name__)
    serve_info = {
        "action":"serve",
        "contents": "正在上菜",
    }
    return json.dumps(serve_info)
# test
