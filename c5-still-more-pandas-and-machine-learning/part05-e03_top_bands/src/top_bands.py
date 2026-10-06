#!/usr/bin/env python3

import pandas as pd

def top_bands():
    uk=pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    band=pd.read_csv("src/bands.tsv", sep="\t")
    band["Band"]=band["Band"].str.upper()
    merged=pd.merge(uk,band,left_on="Artist",right_on="Band")
    return merged
def main():
    print(top_bands())

if __name__ == "__main__":
    main()
