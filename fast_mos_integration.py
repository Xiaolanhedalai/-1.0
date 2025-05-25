import requests

def get_mos_score(audio_path):
    with open(audio_path, "rb") as f:
        resp = requests.post("http://localhost:5000/api/fast_mos", files={"file": f})
        data = resp.json()
        return data.get("mos_score", None)