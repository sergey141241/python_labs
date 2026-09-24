Лабораторная работа №2:


Задание arrays:
1)
```python
def min_max(nums):
    if len(nums) == 0:
        raise ValueError("пустой список")
    return (min(nums), max(nums))

print(min_max([3, -1, 5, 5, 0]))    # (-1, 5)
print(min_max([42]))                # (42, 42)
```


<img width="129" height="52" alt="Image" src="https://github.com/user-attachments/assets/fe3acc9b-59a2-413c-b43d-ffa78ec46d3c" />


если кол-во элементов = 0 то выдает ошибку, если нет то возвращается кортеж из наименьш и наибольш чисел.


2)
```python
def unique_sorted(nums):
    result = []
    for x in nums:
        if x not in result:
            result.append(x)
    result.sort()
    return result

print(unique_sorted([3, 1, 2, 1, 3])) # [1, 2, 3]
print(unique_sorted([])) 
```


<img width="107" height="62" alt="Image" src="https://github.com/user-attachments/assets/3a51768a-79e8-422b-b3cc-47184ad32b61" />

создаем новый пустой список куда будем ложить неповтор и сортиров числа, идем по списку и проверяем если х нет еще в новом списке то добавляем его, потом соритруем и возвращаем результат.



