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
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    if type(fio) != str:
        raise TypeError("ФИО должно быть строкой")
    if type(group) != str:
        raise TypeError("группа должна быть строкой")
    if type(gpa) != float and type(gpa) != int:
        raise TypeError("GPA должно быть числом")

    parts = fio.split()

    if len(parts) < 2:
        raise ValueError("нужно хотя бы фамилия и имя")
    if group.strip() == "":
        raise ValueError("группа пустая")
    surname = parts[0].capitalize()
    initials = ""
    for i in range(1, len(parts)):
        letter = parts[i][0].upper()
        initials = initials + letter + "."

    group = group.strip()

    gpa_str = "{:.2f}".format(gpa)

    result = surname + " " + initials + ", гр. " + group + ", GPA " + gpa_str
    return result
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


распаковываем кортеж rec[0]... , проверяем что данные должны быть в нужном формате,сплит юзаем чтобы разбить и убрать ненужные пробелы в фамилии, если ее длина < 2 то ошибка если группа пустая то ошибка, делаем 1 букву фамилии заглавной остальные строчные. Создаем пустую строку для накопления , идем по всем словам кроме первого , берем первый символ и делаем его заглавным , приклеиваем букву и точку к уже накопленным инициалам. Strip убираем пробелы по краям (очищенная версия). gpa - превращаяем число в строку с 2 точками после запятой с помощью формат подставляем число в образец и собираем всю строчку.








