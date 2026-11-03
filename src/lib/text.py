import re


def normalize(text, *, casefold=True, yo2e=True):
    result = text
    if casefold == True:
        result = result.casefold()
    if yo2e == True:
        result = result.replace("ё", "е").replace("Ё", "Е")
    result = re.sub(r"\s+", " ", result)
    return result.strip()


def tokenize(text):
    return re.findall(r"\w+(?:-\w+)*", text)


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