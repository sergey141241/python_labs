Лабораторная работа №4

Заданиа А:

```python
from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает файл целиком и возвращает его содержимое одной строкой.

    Args:
        path: путь к файлу (строка или Path).
        encoding: кодировка, по умолчанию "utf-8".
            Для другой кодировки укажите например encoding="cp1251".

    Returns:
        Содержимое файла как строка.

    Raises:
        FileNotFoundError: файла нет по указанному пути.
        UnicodeDecodeError: содержимое не читается в этой кодировке.
    """
    return Path(path).read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские папки пути, если их ещё нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: Iterable[Sequence],
              path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Записывает строки в csv-файл с разделителем ",".

    Папки создаются автоматически, старый файл перезаписывается.
    Если header задан — идёт первой строкой.

    Args:
        rows: итерируемое со строками-последовательностями.
        path: путь к CSV-файлу.
        header: необязательный кортеж названий колонок.

    Raises:
        Valueerror: строки разной длины или длина заголовка не совпала.
        Oserror: ошибка создания папок или записи.
    """
    data = list(rows)

    if data:
        size = len(data[0])
        for i, row in enumerate(data, start=1):
            if len(row) != size:
                raise ValueError(
                    f"Строка {i}: {len(row)} значений, ожидалось {size}"
                )
        if header is not None and len(header) != size:
            raise ValueError(
                f"Заголовок: {len(header)} значений, ожидалось {size}"
            )

    p = Path(path)
    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in data:
            w.writerow(r)
```

импортируем нужные библиотеки, создаем функцию и возвращае (path превращает строку в обьект path, открываем файл читаем все содержимое закрывает и возвращает строку). Создаем родительские папки(parents = true - создать всю цепочку сверху вниз, exist_ok = true - не падать если уже есть). write_csv - задаем что то интегрируемое (последоватльность список кортежей иили списков). Превращаем rows в список , чтобы можно было пройти по нему несколько раз , если список не пустой задаем длину (сколько элементов в 1 строке столько и во всех). Идем по строкам , если длина строки не совпадает с эталоном выбрасываем ошибку через Ф строку. Проверяем есть ли заголовок и совпадает по длине с данными , если нет выбрасываем ошибку. Преобразуем путь в path , создаем родит папки если их нет. Открываем файл (w - режим запись, newline - не даем питону самому менять , добавлять переводы строк и пишем в ютф 8) with as f - файл автоматически закроется даже если там ошибка. Создаем обьект в цсв формате , если есть заголовок пишем его 1 строкой, далее проходим по строкам и пишем каждую.


Мини тест:
```python
python -c "from src.lab04.io_txt_csv import read_text; print(read_text('data/lab04/input.txt'))"
python -c "from src.lab04.io_txt_csv import write_csv; write_csv([('word','count'),('test',3)], 'data/lab04/check.csv')"
```


<img width="1209" height="111" alt="Image" src="https://github.com/user-attachments/assets/ce28aaaf-8f6d-484d-aa08-9ef57617f160" />

<img width="289" height="142" alt="Image" src="https://github.com/user-attachments/assets/f59ae12f-9190-4391-bf85-1708f4797e53" />

Первая комнада читает инит, вторая создает чек.цсв


2.
```python
python -c "from src.lab04.io_txt_csv import read_text; print(repr(read_text('data/lab04/empty.txt')))"
```

<img width="1188" height="98" alt="Image" src="https://github.com/user-attachments/assets/3573129f-0117-4a98-b3c0-619a817d9e83" />


Для пустоко файла возвращает пустую строку


3.
```python
python -c "from src.lab04.io_txt_csv import write_csv; write_csv([], 'data/lab04/empty.csv')"
dir data\lab04\empty.csv
```

<img width="243" height="149" alt="Image" src="https://github.com/user-attachments/assets/44e1ee5f-99fe-436e-9a20-15c2f17ec321" />


создается файл с размером 0



4.
```python
python -c "from src.lab04.io_txt_csv import write_csv; write_csv([], 'data/lab04/header_only.csv', header=('a','b'))"
type data\lab04\header_only.csv
```


<img width="352" height="63" alt="Image" src="https://github.com/user-attachments/assets/78ce3ab3-dab3-491e-91d8-0a6c67f23f65" />

пустой rows, выводит только a,b


```python
python -c "from src.lab04.io_txt_csv import write_csv; write_csv([(1,2),(3,)], 'data/lab04/bad.csv')"
```


<img width="942" height="165" alt="Image" src="https://github.com/user-attachments/assets/bece13af-7194-4d9c-87d3-d5ae19e049b1" />


Разная длинна строк вызывает ошибку.


Задание В:

```python
"""
Считает частоты слов входного текста и сохраняет CSV-отчёт.
...
"""

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
```
Импортируем бибилотеки, создаем путь к папке и импортируем функции из 3 лабы. Далее делаем абсолютный путь, чтобы не зависело от того откуда его запускают , также правильно склеиваем части пути. Создаем функцию для сортировки , freq_times -возвращает пары (ключ, значение) и превращаем в список для сортировки. Сортируем , создаем ключ -pair - сортировка по убыванию частоты, pair[0] - если частоты равны , то сортируем по алфавиту по возраст. Создаем парсер аргументов команд строки (парсер -который позволяет скрипту читать параметры, переданные через командную строку при запуске программы) ap - корткое имя что не писать parser. in = входной файл , dest - куда сохранится значение , default - значение по умолочанию. Развибраем аргументы при помощи ap.parse_args() . читаем содержимое файла как одну строку. используем функцию из io_txt_csv. Используем испортируемые ранее функции , превращаем словарь в отсортировачный список пар, пишем csv (он сам создаст родит папки и проверит длинны). Идем по списку бест распаковывем w-слово, с - частота 

Тест:
```python
python src/lab04/text_report.py --in data/lab04/empty.txt --out data/lab04/report_empty.csv; Get-Content data/lab04/report_empty.csv
```

<img width="1155" height="165" alt="Image" src="https://github.com/user-attachments/assets/ede0302e-a734-441e-856d-dedea53021b1" />

Пустой файл, в выводе только заголовок.




