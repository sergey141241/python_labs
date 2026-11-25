import csv
import json
from pathlib import Path

from src.lab08.models import STUDENT_FIELDS, student_from_dict, student_to_dict


def students_to_json(students: list, path) -> None:
    """Сохранить список записей в JSON-массив (ensure_ascii=False, indent=2)."""
    data = [student_to_dict(s) for s in students]
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path) -> list:
    """Прочитать JSON-массив записей. Политика strict: первая битая запись -> ValueError."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    try:
        with p.open(encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"{path}: битый JSON ({e})") from None
    if not isinstance(data, list):
        raise ValueError(f"{path}: ожидался JSON-массив")

    students = []
    for i, item in enumerate(data, start=1):
        try:
            students.append(student_from_dict(item))
        except ValueError as e:
            raise ValueError(f"запись №{i}: {e}") from None
    return students


def students_from_csv(path) -> list:
    """★ Чтение записей из CSV (заголовок fio,birthdate,group,gpa). Политика та же - strict."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    with p.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or tuple(reader.fieldnames) != STUDENT_FIELDS:
            raise ValueError(f"{path}: заголовок должен быть {','.join(STUDENT_FIELDS)}")
        students = []
        # start=2 - первая строка файла это заголовок
        for i, row in enumerate(reader, start=2):
            try:
                students.append(student_from_dict(row))
            except ValueError as e:
                raise ValueError(f"строка {i}: {e}") from None
    return students


if __name__ == "__main__":
    from src.lab08.models import format_student

    students = students_from_json("data/lab08/students_input.json")
    for s in students:
        print(format_student(s))
    students_to_json(students, "data/lab08/students_output.json")
    print("Сохранено в data/lab08/students_output.json")

    try:
        students_from_json("data/lab08/students_bad.json")
    except ValueError as e:
        print("Ошибка в students_bad.json:", e)

    from src.lab08.models import make_student
    try:
        make_student("Смирнова Мария", "2007-07-07", "БИВТ-26-6-2", 7)
    except ValueError as e:
        print("Ошибка make_student:", e)

    print("Из CSV:", students_from_csv("data/lab08/students_input.csv"))
