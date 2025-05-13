# Author: Nanaya
# Description: 语音ui控制
# Created by Nanaya

import re
from typing import List, Optional

# 可识别的动作关键词列表
ACTION_KEYWORDS = [
    "挥手", "点头", "微笑", "眨眼", "鞠躬","跳舞","唱歌","投喂","撒娇","生气",
    "wave", "nod", "smile", "blink", "bow","dance","sing","feed","actcute","angry",
]

def extract_actions(text: str) -> List[str]:
    """
    从回复文本中提取动作指令
    支持#标签动作，也支持自然语言中识别常见动作词
    返回动作列表，例如 ['wave', 'smile']
    """
    actions = []

    # 先提取#动作标签
    matches = re.findall(r"#(\w+)", text)
    if matches:
        actions.extend(matches)

    # 再扫描关键词
    for keyword in ACTION_KEYWORDS:
        if keyword in text and keyword not in actions:
            actions.append(keyword)

    # 去重
    actions = list(set(actions))

    return actions

def extract_primary_action(text: str) -> Optional[str]:
    """
    简单版提取：只返回第一个动作（如果需要单动作控制）
    """
    actions = extract_actions(text)
    return actions[0] if actions else None

