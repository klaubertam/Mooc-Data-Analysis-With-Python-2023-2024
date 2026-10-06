#!/usr/bin/env python3


def main():
    for i in range(1,11):
        string=""
        for j in range(1,11):
            string+=f"{i*j} "
        print(string)

if __name__ == "__main__":
    main()
