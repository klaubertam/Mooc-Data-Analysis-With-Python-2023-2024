#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    return len(df[df["Population change from the previous year, %"]>0])/len(df)

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities = df.iloc[1:312]

    proportion = growing_municipalities(municipalities)

    print(f"Proportion of growing municipalities: {proportion:.1%}")

if __name__ == "__main__":
    main()
