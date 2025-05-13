# Author: Nanaya
# Description: 控制动作映射
# Created by Nanaya

def map_action(cmd):
    if cmd["cmd"] == "adjust_brightness":
        return {"target": "hardware", "api": "set_brightness", "arg": cmd["value"]}
    elif cmd["cmd"] == "avatar_action":
        return {"target": "ui", "api": "do_animation", "arg": cmd["value"]}
    elif cmd["cmd"] == "chat":
        return {"target": "llm", "api": "generate_reply", "arg": cmd["value"]}
    else:
        return {"target": "unknown"}

