from ai_core.facial_expression_engine import generate_expression_v2

def decide_behavior(emotion, context, audio_path):
    expr = generate_expression_v2(emotion, context, None)
    return {
        "expression": expr,
        "emotion": emotion,
        "style": "default",
        "action": None
    }