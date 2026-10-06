import sys

def file_count(filename):
    line_count = 0
    word_count = 0
    char_count = 0

    with open(filename) as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    return line_count, word_count, char_count


def main():
    for filename in sys.argv[1:]:
        lines, words, chars = file_count(filename)

        print(f"{lines}\t{words}\t{chars}\t{filename}")


if __name__ == "__main__":
    main()