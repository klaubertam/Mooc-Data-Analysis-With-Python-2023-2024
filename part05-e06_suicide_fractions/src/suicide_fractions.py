#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df=pd.read_csv("src/who_suicide_statistics.csv",sep=",")
    df["fraction"]=df["suicides_no"]/df["population"]
    df=df.groupby("country")["fraction"].mean()
    return df

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
