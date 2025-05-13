#inerleaver:mic、text、socket、auto_play、stream。interact_type:1、语音/文字交互；2、透传。
# Author: Nanaya
# Description: 添加动作回复
# Created by Nanaya
class Interact:

    def __init__(self, interleaver: str, interact_type: int, data: dict):
        self.interleaver = interleaver
        self.interact_type = interact_type
        self.data = data
