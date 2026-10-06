#!/usr/bin/env python3
import pandas as pd

def read_series():
    s=pd.Series(dtype=object)
    while True:
        line=input()
        if line =="":
            break
        parts=line.split()
        if len(parts)==2:
            s[parts[0]]=parts[1]
        else:
            raise Exception("Malformed input")
    return s
def main():
    print(read_series())

if __name__ == "__main__":
    main()
