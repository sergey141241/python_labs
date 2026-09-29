Лабораторная работа №2:


Задание arrays:

```python
def min_max(nums):
    if len(nums) == 0:
        raise ValueError("пустой список")

    minimum = nums[0]
    maximum = nums[0]

    for x in nums:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return (minimum, maximum)
print(min_max([3, -1, 5, 5, 0]))    # (-1, 5)
print(min_max([42]))                # (42, 42)
```


<img width="129" height="52" alt="Image" src="https://github.com/user-attachments/assets/fe3acc9b-59a2-413c-b43d-ffa78ec46d3c" />


если кол-во элементов = 0 то выдает ошибку, идем по всем элкментам и если нашли то обновляем мин макс. возвращается кортеж из наименьш и наибольш чисел.




```python
def unique_sorted(nums):
    unique = []
    for x in nums:
        found = False
        for u in unique:
            if u == x:
                found = True
        if found == False:
            unique.append(x)

    n = len(unique)
    for i in range(n):
        for j in range(n - 1):
            if unique[j] > unique[j + 1]:
                temp = unique[j]
                unique[j] = unique[j + 1]
                unique[j + 1] = temp
    return unique
print(unique_sorted([3, 1, 2, 1, 3])) # [1, 2, 3]
print(unique_sorted([])) 
```


<img width="107" height="62" alt="Image" src="https://github.com/user-attachments/assets/3a51768a-79e8-422b-b3cc-47184ad32b61" />

создаем новый пустой список куда будем ложить результат, берем каждое число из nums , флаг что число еще не нашли идем по ччислам и сравниваем добавили или нет, если да то поднимаем флаг. Если совпадений не было то добавляем х в результат. Запоминаем длину списка в n , идем for по всем числам и идем по всем парам соседей. Если левое больше правого то сохраняем число в temp, на место левого ставим правое и на месте правого ставим левое из temp и возвращаем


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


```python
def row_sums(mat):
    if len(mat) > 0:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                raise ValueError("рваная матрица")
    result = []
    for row in mat:
        s = 0
        for x in row:
            s = s + x
        result.append(s)
    return result


print(row_sums([[1, 2, 3], [4, 5, 6]]))    # [6, 15]
print(row_sums([[-1, 1], [10, -10]]))      # [0, 0]
print(row_sums([[0, 0], [0, 0]]))          # [0, 0]
```


<img width="97" height="69" alt="Image" src="https://github.com/user-attachments/assets/dae13139-1c5b-4c28-a9a0-0bf27a60238b" />

создаем список для сумм, перебираем строки,обнуляем накопитель перед каждой строкой (строго внутри внеш цикла), перебираем элементы текущей строки и добавляем элемент к сумме и добав сумму в рез


```python
ef col_sums(mat):
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
        s = 0
        for i in range(rows):
            s = s + mat[i][j]
        result.append(s)
    return result


print(col_sums([[1, 2, 3], [4, 5, 6]]))    # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))      # [9, -9]
print(col_sums([[0, 0], [0, 0]]))          # [0, 0]
```


<img width="114" height="63" alt="Image" src="https://github.com/user-attachments/assets/c78db4b1-6152-42d2-8656-630950b820f8" />

если длина 0 то [], считаем кол-во строк и столбцов, создаем список с суммами, идем по столбцам и обнуляем сумму для каждого нового столбца,идем по строкам и обновляем сумма взяв элемент из i-строки и j-столбца и добавляем сумму в результат.



Задание tuples:

```python
def format_record(rec):
    if type(rec) is not tuple:
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:
        raise ValueError("В кортеже должно быть 3 элемента")

    fio = rec[0]
    group = rec[1]
    gpa = rec[2]

    if type(fio) is not str:
        raise TypeError("Имя должно быть строкой")
    if type(group) is not str:
        raise TypeError("Группа должна быть строкой")
    if type(gpa) is not float and type(gpa) is not int:
        raise TypeError("Оценка должна быть числом")
    if gpa < 0.0 or gpa > 5.0:
        raise ValueError("GPA должен быть от 0.0 до 5.0")

    words = fio.strip().split()
    if len(words) != 2 and len(words) != 3:
        raise ValueError("Введено не полное ФИО")
    if len(group.strip()) == 0:
        raise ValueError("Группа не может быть пустой")

    fam = words[0].capitalize()
    name_letter = words[1][0].upper()

    if len(words) == 3:
        otch_letter = words[2][0].upper()
        head = fam + " " + name_letter + "." + otch_letter + "."
    else:
        head = fam + " " + name_letter + "."

    return head + ", гр. " + group + ", GPA " + "{:.2f}".format(gpa)
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# Иванов И.И., гр. BIVT-25, GPA 4.60

print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
# Петров П., гр. IKBO-12, GPA 5.00

print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# Петров П.П., гр. IKBO-12, GPA 5.00

print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
# Сидорова А.С., гр. ABB-01, GPA 4.00
```


<img width="339" height="89" alt="Image" src="https://github.com/user-attachments/assets/c37d2338-ddac-4f6b-ac24-6ac53c36fb9d" />


делаем проверки по тз, распаковывем кортежи , форматируем фамилию стрип убирает пробелы по краям, делаем заглавные буквы , форматируем окончат фамилию, возыращаем строку с форматом gpa 2 числа после







