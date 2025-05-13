# Author: Nanaya
# Description: 指令识别
# Created by Nanaya

def parse_command(text):
    text = text.lower()
    if ("太亮" in text) or ("刺眼" in text):
        return {"cmd": "adjust_brightness", "value": -30}
    elif "太暗" in text:
        return {"cmd": "adjust_brightness", "value": 30}
    elif "打招呼" in text or "你好" in text:
        return {"cmd": "avatar_action", "value": "wave"}
    else:
        return {"cmd": "chat", "value": text}  # fallback to LLM


