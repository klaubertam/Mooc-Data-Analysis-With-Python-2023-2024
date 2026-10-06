#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df=pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";").dropna(how="all").dropna(axis=1, how="all")
    newdf = df["Päivämäärä"].str.split(expand=True)
    newdf = newdf.astype(object)
    newdf.columns=["Weekday","Day","Month","Year","Hour"]
    newdf["Weekday"]=newdf["Weekday"].replace({"ma":"Mon","ti":"Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun"})
    newdf["Month"]=newdf["Month"].replace({
        "tammi": 1,
        "helmi" :2,
        "maalis" :3,
        "huhti" :4,
        "touko" :5,
        "kesä" :6,
        "heinä" :7,
        "elo" :8,
        "syys" :9,
        "loka" :10,
        "marras": 11,
        "joulu" :12})
    newdf["Hour"]=newdf["Hour"].str[:2].astype(int)
    newdf["Day"] = newdf["Day"].astype(int)
    newdf["Month"] = newdf["Month"].astype(int)
    newdf["Year"] = newdf["Year"].astype(int)
    return newdf


def main():
    print(split_date())
       
if __name__ == "__main__":
    main()
