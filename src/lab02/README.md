Лабораторная работа №2:


Задание arrays:

'''python 
def min_max(nums):
    if len(nums) == 0:
        raise ValueError("пустой список")
    return (min(nums), max(nums))

print(min_max([3, -1, 5, 5, 0]))      # (-1, 5)
print(min_max([42]))                   # (42, 42)
'''


