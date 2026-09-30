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


import re

def tokenize(text):
    pattern = r"\w+(?:-\w+)*"
    return re.findall(pattern, text)



def count_freq(tokens):
    freq = {}
    for word in tokens:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq


def top_n(freq, n=5):
    items = []
    for word in freq:
        items.append((word, freq[word]))

    items.sort(key=lambda pair: (-pair[1], pair[0]))

    return items[:n]

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
print(count_freq(["a", "b", "a", "c", "b", "a"]))
print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), 2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), 2))