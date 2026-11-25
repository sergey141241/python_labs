import argparse
import sys

from src.lab08.models import format_student, make_student
from src.lab09.group import (
    add_student,
    find_students,
    list_students,
    remove_student,
    stats,
    update_student,
)

DEFAULT_DB = "data/lab09/students.csv"


def print_students(students: list) -> None:
    if not students:
        print("(пусто)")
    for s in students:
        print(format_student(s))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="CLI-база студентов лабораторной №9")
    parser.add_argument("--db", default=DEFAULT_DB, help=f"Путь к CSV (по умолчанию {DEFAULT_DB})")
    subparsers = parser.add_subparsers(dest="command")

    add_p = subparsers.add_parser("add", help="Добавить студента")
    add_p.add_argument("--fio", required=True)
    add_p.add_argument("--birthdate", required=True, help="YYYY-MM-DD")
    add_p.add_argument("--group", required=True)
    add_p.add_argument("--gpa", required=True, type=float)

    list_p = subparsers.add_parser("list", help="Список студентов")
    list_p.add_argument("--sort", choices=["fio", "gpa"], default=None)

    find_p = subparsers.add_parser("find", help="Поиск по подстроке в ФИО")
    find_p.add_argument("--q", required=True)

    remove_p = subparsers.add_parser("remove", help="Удалить по ФИО")
    remove_p.add_argument("--fio", required=True)

    update_p = subparsers.add_parser("update", help="Обновить поля студента")
    update_p.add_argument("--fio", required=True)
    update_p.add_argument("--gpa", type=float)
    update_p.add_argument("--group")
    update_p.add_argument("--birthdate")

    subparsers.add_parser("stats", help="Статистика по группе")

    args = parser.parse_args(argv)

    if args.command is None:
        parser.error("Не указана подкоманда (add, list, find, remove, update, stats)")

    try:
        if args.command == "add":
            s = make_student(args.fio, args.birthdate, args.group, args.gpa)
            add_student(args.db, s)
            print("Добавлен:", format_student(s))
        elif args.command == "list":
            print_students(list_students(args.db, args.sort))
        elif args.command == "find":
            print_students(find_students(args.db, args.q))
        elif args.command == "remove":
            n = remove_student(args.db, args.fio)
            print(f"Удалено записей: {n}")
        elif args.command == "update":
            fields = {}
            for k in ("gpa", "group", "birthdate"):
                v = getattr(args, k)
                if v is not None:
                    fields[k] = v
            if not fields:
                parser.error("update: укажите хотя бы одно из --gpa, --group, --birthdate")
            if update_student(args.db, args.fio, **fields):
                print("Обновлено:", args.fio)
            else:
                print(f"Ошибка: студент '{args.fio}' не найден", file=sys.stderr)
                return 1
        elif args.command == "stats":
            st = stats(args.db)
            print("Всего студентов:", st["count"])
            print("GPA мин / макс / средний:", st["min_gpa"], "/", st["max_gpa"], "/", st["avg_gpa"])
            print("По группам:")
            for g, n in st["groups"].items():
                print(f"  {g}: {n}")
            print("Топ-5:")
            for i, s in enumerate(st["top_5_students"], start=1):
                print(f"  {i}. {s['fio']} - {s['gpa']:.2f}")
    except (ValueError, KeyError) as e:
        print("Ошибка:", e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
