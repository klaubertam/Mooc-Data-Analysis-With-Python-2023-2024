#!/usr/bin/env python3

def distinct_characters(L):
    d={}
    for element in L:
        d[element]=len(set(element))
    return d

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
