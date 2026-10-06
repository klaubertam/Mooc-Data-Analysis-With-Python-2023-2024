#!/usr/bin/env python3

def extract_numbers(s):
    parts=s.split(" ")
    newlist=[]
    for part in parts:
        try:
            x=int(part)
            newlist.append(x)
        except Exception:
            try:
                y=float(part)
                newlist.append(y)
            except Exception:
                continue
    return newlist

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
