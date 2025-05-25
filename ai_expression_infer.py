class DummyExpressionModel:
    def predict(self, emotion, context, audio_features):
        # 这里用简单规则模拟，实际项目推荐替换为深度学习模型
        base = {
            "smile": 0.7 if emotion=="happy" else 0.1,
            "mouth_open": 0.2 if emotion in ["happy","surprised"] else 0.1,
            "brow_raise": 0.6 if emotion=="surprised" else 0.3,
            "eye_blink": 0.1
        }
        return base