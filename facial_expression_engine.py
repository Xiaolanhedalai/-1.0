def generate_expression_v2(emotion, context, audio_features=None, style="default"):
    # 简化：返回预设表情
    preset = {
        "happy": {"smile": 1.0, "eye_blink": 0.0},
        "sad": {"smile": 0.0, "eye_blink": 0.5},
        "angry": {"smile": 0.0, "brow_frown": 1.0},
        "surprised": {"smile": 0.0, "mouth_open": 1.0},
        "confused": {"smile": 0.0, "brow_raise": 1.0},
        "neutral": {"smile": 0.0, "eye_blink": 0.0}
    }
    return preset.get(emotion, preset["neutral"])