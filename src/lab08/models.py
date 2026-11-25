from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def _check_text(name: str, value) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{name}: ожидалась строка, получено {type(value).__name__}")
    value = value.strip()
    if not value:
        raise ValueError(f"{name}: пустая строка")
    return value


def _check_birthdate(value) -> str:
    if not isinstance(value, str):
        raise ValueError(f"birthdate: ожидалась строка, получено {type(value).__name__}")
    try:
        d = date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"birthdate: '{value}' не дата в формате YYYY-MM-DD") from None
    # fromisoformat в новых версиях понимает и 20070514, нам нужен строго YYYY-MM-DD
    if d.isoformat() != value:
        raise ValueError(f"birthdate: '{value}' не дата в формате YYYY-MM-DD")
    if d > date.today():
        raise ValueError(f"birthdate: '{value}' дата в будущем")
    return value


def _check_gpa(value) -> float:
    # bool это подкласс int, True прошел бы как 1, поэтому отсекаем отдельно
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"gpa: ожидалось число, получено {type(value).__name__}")
    if not (0 <= value <= 5):
        raise ValueError(f"gpa: {value} вне диапазона 0..5")
    return float(value)


def make_student(fio, birthdate, group, gpa) -> dict:
    """Собрать запись студента, проверив каждое поле.

    make_student("Иванов Иван Иванович", "2007-05-14", "БИВТ-26-6-1", 4.3)
    -> {"fio": "Иванов Иван Иванович", "birthdate": "2007-05-14", "group": "БИВТ-26-6-1", "gpa": 4.3}
    """
    return {
        "fio": _check_text("fio", fio),
        "birthdate": _check_birthdate(birthdate),
        "group": _check_text("group", group),
        "gpa": _check_gpa(gpa),
    }


def validate_student(rec: dict) -> None:
    """Проверить готовую запись: набор ключей и значения. При ошибке ValueError."""
    if not isinstance(rec, dict):
        raise ValueError(f"запись должна быть словарем, получено {type(rec).__name__}")
    if set(rec) != set(STUDENT_FIELDS):
        missing = [k for k in STUDENT_FIELDS if k not in rec]
        extra = [str(k) for k in rec if k not in STUDENT_FIELDS]
        msg = []
        if missing:
            msg.append("нет полей: " + ", ".join(missing))
        if extra:
            msg.append("лишние поля: " + ", ".join(extra))
        raise ValueError("; ".join(msg))
    make_student(rec["fio"], rec["birthdate"], rec["group"], rec["gpa"])


def student_age(rec: dict, today=None) -> int:
    """Полных лет на дату today (по умолчанию сегодня).

    student_age({..."birthdate": "2007-09-20"...}, date(2026, 9, 19)) -> 18
    student_age({..."birthdate": "2007-09-20"...}, date(2026, 9, 20)) -> 19
    """
    b = date.fromisoformat(rec["birthdate"])
    if today is None:
        today = date.today()
    age = today.year - b.year
    # если день рождения в этом году еще не наступил - минус год
    if (today.month, today.day) < (b.month, b.day):
        age -= 1
    return age


def _years_word(n: int) -> str:
    if n % 10 == 1 and n % 100 != 11:
        return "год"
    if 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
        return "года"
    return "лет"


def _short_fio(fio: str) -> str:
    # как в лаб1: от имени и отчества берем первые буквы, фамилию оставляем целиком
    parts = fio.split()
    initials = ""
    for p in parts[1:]:
        initials = initials + p[0].upper() + "."
    if initials:
        return parts[0] + " " + initials
    return parts[0]


def format_student(rec: dict, today=None) -> str:
    """Иванов И.И. (БИВТ-26-6-1), 19 лет, GPA 4.30"""
    age = student_age(rec, today)
    return f"{_short_fio(rec['fio'])} ({rec['group']}), {age} {_years_word(age)}, GPA {rec['gpa']:.2f}"


def student_to_dict(rec: dict) -> dict:
    """Копия записи для сериализации (новый словарь, а не rec)."""
    validate_student(rec)
    return {k: rec[k] for k in STUDENT_FIELDS}


def student_from_dict(d: dict) -> dict:
    """Десериализация: ровно нужные ключи, gpa -> float, валидация."""
    if not isinstance(d, dict):
        raise ValueError(f"запись должна быть словарем, получено {type(d).__name__}")
    missing = [k for k in STUDENT_FIELDS if k not in d]
    if missing:
        raise ValueError("нет полей: " + ", ".join(missing))
    gpa = d["gpa"]
    # из CSV gpa приходит строкой - здесь это и лечится
    if isinstance(gpa, str):
        try:
            gpa = float(gpa.replace(",", "."))
        except ValueError:
            raise ValueError(f"gpa: '{d['gpa']}' не число") from None
    return make_student(d["fio"], d["birthdate"], d["group"], gpa)


def update_student(rec: dict, **fields) -> dict:
    """★ Новая запись с измененными полями, исходная не меняется.

    s2 = update_student(s1, gpa=4.8); s1["gpa"] - прежнее значение
    """
    for k in fields:
        if k not in STUDENT_FIELDS:
            raise KeyError(f"неизвестное поле: {k}")
    new = dict(rec)
    new.update(fields)
    validate_student(new)
    return make_student(new["fio"], new["birthdate"], new["group"], new["gpa"])
