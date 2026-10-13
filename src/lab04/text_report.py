
import sys
import os
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IN_DEFAULT = os.path.join(ROOT, "data", "lab04", "input.txt")
OUT_DEFAULT = os.path.join(ROOT, "data", "lab04", "report.csv")


def sort_rows(freq):
    """Пары (слово, частота): сначала по частоте ↓, потом по слову ↑."""
    result = list(freq.items())
    result.sort(key=lambda pair: (-pair[1], pair[0]))
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", default=IN_DEFAULT)
    ap.add_argument("--out", dest="out_path", default=OUT_DEFAULT)
    ap.add_argument("--encoding", default="utf-8")
    args = ap.parse_args()

    source = read_text(args.in_path, encoding=args.encoding)

    source = normalize(source)
    words = tokenize(source)
    freq = count_freq(words)
    best = top_n(freq, 5)

    rows = sort_rows(freq)
    write_csv(rows, args.out_path, header=("word", "count"))

    print("Всего слов: " + str(len(words)))
    print("Уникальных слов: " + str(len(freq)))
    print("Топ-5:")
    for w, c in best:
        print(w + ":" + str(c))


if __name__ == "__main__":
    main()