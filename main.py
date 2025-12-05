from pipelines import pipeline
import json


json_file_path = "./data/dct_userguide/userguide-content.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

if isinstance(data, list):
    nlp = pipeline("question_generation")
    for item in data:
        para = item.get("content", None)
        if para:
            output = nlp(para)
            print(f"Output is: {output}\n")
        else:
            print("paragraph is None")
