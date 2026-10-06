#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df=pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    df["LW"]=df["LW"].replace(["New","Re"],np.nan)
    return df[pd.to_numeric(df["LW"])<pd.to_numeric(df["Pos"])]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
