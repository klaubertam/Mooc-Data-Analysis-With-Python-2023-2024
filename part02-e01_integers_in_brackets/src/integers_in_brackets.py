import re

def integers_in_brackets(text):
    pattern = r"\[\s*([+-]?\d+)\s*\]"
    matches = re.findall(pattern, text)
    return [int(num) for num in matches]

def main():
    s = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    print(integers_in_brackets(s))

if __name__ == "__main__":
    main()