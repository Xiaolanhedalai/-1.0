FACIAL_CHANNELS = [
    "smile", "mouth_open", "brow_raise", "brow_frown", "eye_widen", "eye_squint",
    "eye_blink", "cheek_raise", "jaw_drop", "lip_purse", "nose_wrinkle",
    "left_eye_blink", "right_eye_blink", "tongue_out", "nostril_flare"
]

EXPRESSION_PRESETS = {
    "natural_smile": {"smile": 0.7, "eye_squint": 0.3, "cheek_raise": 0.2},
    "sad": {"smile": 0.1, "brow_frown": 0.7, "lip_purse": 0.4, "eye_blink": 0.1},
    "surprised": {"eye_widen": 0.8, "brow_raise": 0.7, "jaw_drop": 0.6},
    "confused": {"smile": 0.1, "brow_frown": 0.8, "mouth_open": 0.2, "eye_blink": 0.3},
    "angry": {"brow_frown": 0.9, "mouth_open": 0.3, "nose_wrinkle": 0.4},
    "shy": {"smile": 0.3, "brow_frown": 0.2, "cheek_raise": 0.1, "eye_blink": 0.2}
}