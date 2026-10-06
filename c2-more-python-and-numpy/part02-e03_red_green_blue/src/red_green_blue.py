#!/usr/bin/env python3

import re

def red_green_blue():
    result = []

    with open("src/rgb.txt") as file:
        next(file)  # remove the first irrelevant line

        for line in file:
            pattern = r"\s*(\d+)\s+(\d+)\s+(\d+)\s+(.*)"

            match = re.search(pattern, line)

            if match:
                red = match.group(1)
                green = match.group(2)
                blue = match.group(3)
                name = match.group(4).strip()

                result.append(f"{red}\t{green}\t{blue}\t{name}")

    return result


def main():
    pass

if __name__ == "__main__":
    main()
