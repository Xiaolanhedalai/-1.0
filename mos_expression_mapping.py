MOS_EXPRESSION_MAPPING = [
    {
        "min": 0.0, "max": 2.5,
        "emotion": "confused",
        "style": "hesitant",
        "expression_weights": {"smile": 0.1, "brow_frown": 0.7, "mouth_open": 0.2, "eye_blink": 0.4},
        "action": "shrug"
    },
    {
        "min": 2.5, "max": 3.5,
        "emotion": "neutral",
        "style": "default",
        "expression_weights": {"smile": 0.3, "brow_frown": 0.4, "mouth_open": 0.3, "eye_blink": 0.2},
        "action": "nod"
    },
    {
        "min": 3.5, "max": 4.2,
        "emotion": "happy",
        "style": "natural",
        "expression_weights": {"smile": 0.7, "brow_frown": 0.1, "mouth_open": 0.3, "eye_blink": 0.1},
        "action": "wave"
    },
    {
        "min": 4.2, "max": 5.0,
        "emotion": "confident",
        "style": "confident",
        "expression_weights": {"smile": 1.0, "brow_frown": 0.0, "mouth_open": 0.4, "eye_blink": 0.05},
        "action": "thumbs_up"
    }
]

def map_mos_to_expression(mos_score):
    for item in MOS_EXPRESSION_MAPPING:
        if item["min"] <= mos_score < item["max"]:
            return item
    return MOS_EXPRESSION_MAPPING[1]