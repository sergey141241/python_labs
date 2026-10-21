import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    p_in = Path(json_path)
    if not p_in.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    try:
        with p_in.open(encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not data or not isinstance(data, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")
        
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON должен содержать список словарей")

    keys = list(data[0].keys())
    for item in data:
        for k in item.keys():
            if k not in keys:
                keys.append(k)

    p_out = Path(csv_path)
    p_out.parent.mkdir(parents=True, exist_ok=True)

    with p_out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    p_in = Path(csv_path)
    if not p_in.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with p_in.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV не содержит заголовка")
        data = list(reader)

    if not data:
        raise ValueError("Пустой CSV")

    p_out = Path(json_path)
    p_out.parent.mkdir(parents=True, exist_ok=True)

    with p_out.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)