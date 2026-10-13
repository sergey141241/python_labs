from pathlib import Path
import csv


def read_text(path, encoding="utf-8"):
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows, path, header=None):
    rows = list(rows)

    lengths = set()
    for row in rows:
        lengths.add(len(row))
    if len(lengths) > 1:
        raise ValueError("все строки должны быть одинаковой длины")

    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def ensure_parent_dir(path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)