import json
from typing import Any


def load_json(json_path: str):
    with open(json_path, "r") as f:
        json_data = json.load(f)
    return json_data


def save_json(json_data: dict[str, Any], json_path: str):
    with open(json_path, "w") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def save_json_list(json_list: list[dict[str, str]], json_path: str):
    with open(json_path, "w") as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)
