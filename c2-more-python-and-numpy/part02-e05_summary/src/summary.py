import sys
import math

def summary(filename):
    numbers = []

    with open(filename) as file:
        for line in file:
            try:
                number = float(line)
                numbers.append(number)
            except ValueError:
                continue

    total = sum(numbers)
    average = total / len(numbers)

    variance = sum((x - average) ** 2 for x in numbers) / (len(numbers) - 1)
    stddev = math.sqrt(variance)

    return total, average, stddev


def main():
    for filename in sys.argv[1:]:
        total, average, stddev = summary(filename)

        print(f"File: {filename} Sum: {total:.6f} "
              f"Average: {average:.6f} "
              f"Stddev: {stddev:.6f}")


if __name__ == "__main__":
    main()