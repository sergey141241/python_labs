def min_max(nums):
    if len(nums) == 0:
        raise ValueError("пустой список")
    return (min(nums), max(nums))

print(min_max([3, -1, 5, 5, 0]))      # (-1, 5)
print(min_max([42]))                   # (42, 42)


def unique_sorted(nums):
    result = []
    for x in nums:
        if x not in result:
            result.append(x)
    result.sort()
    return result

print(unique_sorted([3, 1, 2, 1, 3])) # [1, 2, 3]
print(unique_sorted([]))               # []

def flatten(mat):
    result = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError("это не список или не кортеж")
        for item in row:
            result.append(item)
    return result


print(flatten([[1, 2], (3, 4, 5)]))   # [1, 2, 3, 4, 5]
