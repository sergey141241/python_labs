import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n


def cmd_cat(input_path: str, number: bool) -> None:
    p = Path(input_path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    with p.open(encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if number:
                print(f"{i:>4}  {line}")
            else:
                print(line)


def cmd_stats(input_path: str, top: int) -> None:
    p = Path(input_path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    text = p.read_text(encoding="utf-8")
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print("Всего слов: " + str(len(tokens)))
    print("Уникальных слов: " + str(len(freq)))
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(word + ":" + str(count))


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов вывести (по умолчанию 5)")

    args = parser.parse_args()

    if args.command is None:
        parser.error("Не указана подкоманда (cat или stats)")

    try:
        if args.command == "cat":
            cmd_cat(args.input, args.n)
        elif args.command == "stats":
            if args.top <= 0:
                parser.error("--top должен быть больше 0")
            cmd_stats(args.input, args.top)
    except FileNotFoundError as e:
        parser.error(str(e))


if __name__ == "__main__":
    main()
