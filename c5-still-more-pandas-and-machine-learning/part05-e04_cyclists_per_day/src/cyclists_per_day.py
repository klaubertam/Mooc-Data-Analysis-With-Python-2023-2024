#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date(df):
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

def split_date_continues():
    df=pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    df=df.dropna(how="all")
    df=df.dropna(how="all",axis=1)
    newdf=split_date(df)
    df=df.drop(columns="Päivämäärä")
    df=pd.concat([newdf,df],axis=1)
    return df

def cyclists_per_day():
    df = split_date_continues()
    df = df.drop(columns=["Hour", "Weekday"])
    daily = df.groupby(["Year", "Month", "Day"]).sum()
    return daily

    
def main():
    df=cyclists_per_day()
    august=df.loc[2017,8]
    august.plot()
    plt.show()

if __name__ == "__main__":
    main()
