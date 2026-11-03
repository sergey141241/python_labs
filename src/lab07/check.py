import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def random_list(max_len: int = 50) -> list:
    n = random.randint(0, max_len)
    return [random.randint(-100, 100) for _ in range(n)]


def check_sorting(fn, trials: int = 100) -> int:
    for _ in range(trials):
        nums = random_list()
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список: {original} -> {nums}"
    # отдельно крайние случаи
    for nums in ([], [5], [2, 2, 2], [3, 2, 1], [1, 2, 3]):
        assert fn(nums) == sorted(nums), f"{fn.__name__} ошиблась на {nums}"
    return trials + 5


def check_search(trials: int = 100) -> int:
    count = 0
    for _ in range(trials):
        nums = random_list()
        x = random.randint(-100, 100)
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        got = linear_search(nums, x)
        assert got == expected, f"linear_search({nums}, {x}) = {got}, ожидалось {expected}"
        count += 1

        s = sorted(nums)
        # x которого может не быть, крайние элементы и число вне диапазона
        queries = [x, 1000, -1000]
        if s:
            queries += [s[0], s[-1]]
        for q in queries:
            got = binary_search(s, q)
            if q in s:
                assert got != -1 and s[got] == q, f"binary_search({s}, {q}) = {got}"
            else:
                assert got == -1, f"binary_search({s}, {q}) = {got}, ожидалось -1"
            count += 1
    return count


def check_two_sum(trials: int = 100) -> int:
    for _ in range(trials):
        nums = random_list(30)
        target = random.randint(-200, 200)
        a = two_sum_brute(nums, target)
        b = two_sum_fast(nums, target)
        if a is None or b is None:
            assert a is None and b is None, f"two_sum на {nums}, target={target}: {a} и {b}"
            continue
        for i, j in (a, b):
            assert i < j and nums[i] + nums[j] == target, \
                f"two_sum на {nums}, target={target}: неверная пара ({i}, {j})"
    return trials


if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок")
