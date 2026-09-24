Лабораторная работа №2:


Задание arrays:

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



```python
def flatten(mat):
    result = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError("это не список или не кортеж")
        for item in row:
            result.append(item)
    return result


print(flatten([[1, 2], (3, 4, 5)]))   # [1, 2, 3, 4, 5]
```


<img width="165" height="33" alt="Image" src="https://github.com/user-attachments/assets/c93e41c4-2726-402d-b7df-0708da2da218" />

создаем пустой список с результатом идем по строкам матрицы если строка не список или не кортеж, то выдает ошибку, идем по элементам текущей строки и добавляем элем. в результат, возвращаем его.


Задание matrix:

```python
def transpose(mat):
    if len(mat) > 0:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                raise ValueError("рваная матрица")
    if len(mat) == 0:
        return []
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(mat[i][j])
        result.append(new_row)
    return result


print(transpose([[1, 2, 3]]))       # [[1], [2], [3]]
print(transpose([[1], [2], [3]]))   # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([])) 
```

<img width="175" height="86" alt="Image" src="https://github.com/user-attachments/assets/d2de4aed-5e37-439c-bb1f-d03d9bedd324" />

проверяем матрицу на прямоугольность (длина > 0, создаем переменную куда считаем длину 1 строки, идем дальше по строкам если длина не равно этой переменной то матрицы рванная). Считаем кол во строк и столбцов, идем по столбцам, делаем новую строку реза, идем по строкам , берем элеметы из i-строки и из j-строки таким образом переворачиваем матрицу.




