#!/usr/bin/env python3

def word_frequencies(filename):
    frequencies = {}

    punctuation = """!"#$%&'()*,-./:;?@[]_"""

    with open(filename) as file:
        for line in file:
            for word in line.split():
                word = word.strip(punctuation)

                if word not in frequencies:
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1

    return frequencies

def main():
    freqs = word_frequencies("alice.txt")

    for word, count in freqs.items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
