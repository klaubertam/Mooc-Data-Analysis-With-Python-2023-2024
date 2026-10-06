#!/usr/bin/env python3

import pandas as pd

def cyclists():
    return (
        pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
        .dropna(how="all")
        .dropna(axis=1, how="all")
    )
def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
