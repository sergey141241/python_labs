import random
import timeit

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

# квадратичные сортировки на 10^5 не запускаем: ~10^10 шагов, это полчаса
QUADRATIC_LIMIT = 10_000


def bench_sorts(n: int) -> list:
    data = [random.randint(-10**6, 10**6) for _ in range(n)]
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))
    for fn in (bubble_sort, insertion_sort, selection_sort):
        if n > QUADRATIC_LIMIT:
            rows.append(("sort", n, fn.__name__, "> 60"))
            continue
        t = timeit.timeit(lambda: fn(data), number=1)
        rows.append(("sort", n, fn.__name__, t))
    return rows


def bench_search(n: int = 100_000, queries: int = 10_000) -> list:
    data = [random.randint(0, 10 * n) for _ in range(n)]
    qs = [random.randint(0, 10 * n) for _ in range(queries)]
    rows = []

    t = timeit.timeit(lambda: [linear_search(data, q) for q in qs], number=1)
    rows.append(("search", n, "linear_search", t))

    s = []
    t = timeit.timeit(lambda: s.extend(sorted(data)), number=1)
    rows.append(("search", n, "sorted (для binary)", t))

    t = timeit.timeit(lambda: [binary_search(s, q) for q in qs], number=1)
    rows.append(("search", n, "binary_search", t))
    return rows


def bench_two_sum(n: int) -> list:
    data = random.sample(range(-10 * n, 10 * n), n)
    # ответ гарантированно есть - сумма двух последних
    target = data[-2] + data[-1]
    rows = []
    for fn in (two_sum_brute, two_sum_fast):
        t = timeit.timeit(lambda: fn(data, target), number=1)
        rows.append(("two_sum", n, fn.__name__, t))
    return rows


def fmt(seconds) -> str:
    if isinstance(seconds, str):
        return seconds
    return f"{seconds:.6f}"


def main():
    random.seed(42)
    rows = []
    for n in (1_000, 10_000, 100_000):
        rows += bench_sorts(n)
    rows += bench_search()
    for n in (1_000, 10_000):
        rows += bench_two_sum(n)

    rows = [(task, n, impl, fmt(t)) for task, n, impl, t in rows]

    print(f"{'task':<8} {'n':>7}  {'impl':<20} {'seconds':>10}")
    print("-" * 49)
    for task, n, impl, t in rows:
        print(f"{task:<8} {n:>7}  {impl:<20} {t:>10}")

    write_csv(rows, "data/lab07/bench.csv", header=("task", "n", "impl", "seconds"))
    print("\nСохранено в data/lab07/bench.csv")


if __name__ == "__main__":
    main()
