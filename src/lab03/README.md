Лабораторная работа №3

Задание А:

```python
import re

def normalize(text, *, casefold=True, yo2e=True):
    result = text

    if casefold == True:
        result = result.casefold()

    if yo2e == True:
        result = result.replace("ё", "е")
        result = result.replace("Ё", "Е")

    result = re.sub(r"\s+", " ", result)
    result = result.strip()

    return result
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```


<img width="164" height="89" alt="Image" src="https://github.com/user-attachments/assets/01a39a68-b88d-4e1f-b925-09120ac37929" />


импортим re, если флаг включен , то превращаем все буквы в нижний регистр (для юникода), если нужно менять е на ё , меняем. регуляркой ищем и заменяем лишние пробелы ((r'\s+') 1 или больше пробелов ) 

