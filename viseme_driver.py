def phoneme_to_blendshape(phoneme):
    mapping = {
        "A": {"mouth_open": 0.8, "jaw_drop": 0.6},
        "O": {"mouth_open": 0.6, "lip_purse": 0.4},
        "E": {"mouth_open": 0.7},
        "M": {"mouth_open": 0.2, "lip_purse": 0.7},
        "I": {"mouth_open": 0.5, "smile": 0.3},
        "U": {"mouth_open": 0.4, "lip_purse": 0.8}
    }
    return mapping.get(phoneme, {})

def viseme_sequence(phoneme_sequence):
    return [phoneme_to_blendshape(p) for p in phoneme_sequence]