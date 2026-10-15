from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает файл целиком и возвращает его содержимое одной строкой.

    Args:
        path: путь к файлу (строка или Path).
        encoding: кодировка, по умолчанию "utf-8".
            Для другой кодировки укажите явно, например encoding="cp1251".

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