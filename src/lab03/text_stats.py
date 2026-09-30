import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.text import normalize, tokenize, count_freq, top_n


def read_input():
    data = sys.stdin.buffer.read()
    for enc in ("utf-8", "cp1251", "cp866"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


text = read_input()
text = normalize(text)
tokens = tokenize(text)
freq = count_freq(tokens)
top = top_n(freq, 5)

print("Всего слов: " + str(len(tokens)))
print("Уникальных слов: " + str(len(freq)))
print("Топ-5:")
for word, count in top:
    print(word + ":" + str(count))