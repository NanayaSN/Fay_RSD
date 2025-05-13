# Author: Nanaya
# Description: 控制调度器（UI+硬件）
# Created by Nanaya

def dispatch(action):
    if action["target"] == "hardware":
        from hardware import brightness
        brightness.set_brightness(action["arg"])
    elif action["target"] == "ui":
        from ui import socket_client
        socket_client.send_action(action["api"], action["arg"])
    elif action["target"] == "llm":
        from llm import chatgpt
        response = chatgpt.get_response(action["arg"])
        print("LLM Response:", response)
    else:
        print("Unknown action, skipping.")