import csv
from pathlib import Path

from src.lab08.models import STUDENT_FIELDS, student_from_dict, validate_student

HEADER = STUDENT_FIELDS


def ensure_storage(path) -> None:
    """Создать файл с одной строкой-заголовком, если его еще нет (вместе с папками)."""
    p = Path(path)
    if p.exists():
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(HEADER)


def load_students(path) -> list:
    """Все записи из CSV, каждая строка через student_from_dict."""
    ensure_storage(path)
    with Path(path).open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError(f"{path}: нет строки-заголовка")
        if tuple(reader.fieldnames) != HEADER:
            raise ValueError(
                f"{path}: заголовок {','.join(reader.fieldnames)}, ожидалось {','.join(HEADER)}"
            )
        students = []
        # start=2 - первая строка файла это заголовок
        for i, row in enumerate(reader, start=2):
            # лишние значения в строке DictReader складывает под ключ None
            if None in row:
                raise ValueError(f"{path}, строка {i}: лишние колонки")
            try:
                students.append(student_from_dict(row))
            except ValueError as e:
                raise ValueError(f"{path}, строка {i}: {e}") from None
    return students


def save_students(path, students: list) -> None:
    """Перезаписать файл целиком."""
    for s in students:
        validate_student(s)
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(students)


def add_student(path, student: dict) -> None:
    """Проверить запись и дописать в конец. ★ Дубликат по fio - ValueError."""
    validate_student(student)
    students = load_students(path)
    for s in students:
        if s["fio"] == student["fio"]:
            raise ValueError(f"студент '{student['fio']}' уже есть")
    students.append(dict(student))
    save_students(path, students)


def list_students(path, sort_by=None) -> list:
    """Все студенты, sort_by: None, "fio" или "gpa" (по убыванию)."""
    students = load_students(path)
    if sort_by is None:
        return students
    if sort_by == "fio":
        return sorted(students, key=lambda s: s["fio"].lower())
    if sort_by == "gpa":
        return sorted(students, key=lambda s: s["gpa"], reverse=True)
    raise ValueError(f"неизвестное поле сортировки: {sort_by} (можно fio или gpa)")


def find_students(path, substr: str) -> list:
    """Записи, у которых substr входит в fio без учета регистра."""
    q = substr.casefold()
    return [s for s in load_students(path) if q in s["fio"].casefold()]


def remove_student(path, fio: str) -> int:
    """Удалить все записи с таким fio, вернуть сколько удалено."""
    students = load_students(path)
    left = [s for s in students if s["fio"] != fio]
    removed = len(students) - len(left)
    if removed:
        save_students(path, left)
    return removed


def update_student(path, fio: str, **fields) -> bool:
    """Обновить поля первой записи с таким fio. True если нашли, иначе False."""
    for k in fields:
        if k not in HEADER:
            raise KeyError(f"неизвестное поле: {k}")
    students = load_students(path)
    for i, s in enumerate(students):
        if s["fio"] == fio:
            new = dict(s)
            new.update(fields)
            # прогоняем через student_from_dict: gpa может прийти строкой
            students[i] = student_from_dict(new)
            save_students(path, students)
            return True
    return False


def stats(path) -> dict:
    """★ Статистика по студентам."""
    students = load_students(path)
    if not students:
        return {"count": 0, "min_gpa": None, "max_gpa": None, "avg_gpa": None,
                "groups": {}, "top_5_students": []}
    gpas = [s["gpa"] for s in students]
    groups = {}
    for s in students:
        groups[s["group"]] = groups.get(s["group"], 0) + 1
    top = sorted(students, key=lambda s: s["gpa"], reverse=True)[:5]
    return {
        "count": len(students),
        "min_gpa": min(gpas),
        "max_gpa": max(gpas),
        "avg_gpa": round(sum(gpas) / len(gpas), 2),
        "groups": groups,
        "top_5_students": [{"fio": s["fio"], "gpa": s["gpa"]} for s in top],
    }
