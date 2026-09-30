import sys
sys.path.append("src")

from lib.text import normalize, tokenize, count_freq, top_n

def main():
    text = sys.stdin.read()

    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freq(tokens)
    top = top_n(freq, 5)

    print("Всего слов: " + str(len(tokens)))
    print("Уникальных слов: " + str(len(freq)))
    print("Топ-5:")
    for word, count in top:
        print(word + ":" + str(count))

if __name__ == "__main__":
    main()