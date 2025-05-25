import random
import time

def should_trigger_blink(last_blink_time, interval=3.0):
    # 每隔 interval 秒触发一次眨眼
    return (time.time() - last_blink_time) > random.uniform(interval, interval+1.0)

def get_micro_expression(emotion):
    # 按情绪选择微表情
    micro_map = {
        "happy": ["blink", "cheek_raise"],
        "sad": ["blink", "lip_purse"],
        "surprised": ["brow_raise", "left_eye_blink"],
        "confused": ["brow_frown", "blink"]
    }
    return random.choice(micro_map.get(emotion, ["blink"]))