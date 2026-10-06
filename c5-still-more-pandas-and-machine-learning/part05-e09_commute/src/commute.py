#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def bicycle_timeseries():
    bicycle = pd.read_csv(
        "src/Helsingin_pyorailijamaarat.csv",
        sep=";"
    ).dropna(how="all").dropna(axis=1, how="all")

    newdf = bicycle["Päivämäärä"].str.split(expand=True)
    newdf.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    newdf["Weekday"] = newdf["Weekday"].replace({
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun"
    })

    newdf["Month"] = newdf["Month"].replace({
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12
    })

    newdf["Hour"] = newdf["Hour"].str[:2].astype(int)
    newdf["Day"] = newdf["Day"].astype(int)
    newdf["Month"] = newdf["Month"].astype(int)
    newdf["Year"] = newdf["Year"].astype(int)

    # Remove original date column first
    bicycle = bicycle.drop(columns=["Päivämäärä"])

    # Add parsed date columns
    bicycle = pd.concat([bicycle, newdf], axis=1)

    bicycle["Date"] = pd.to_datetime(
        bicycle[["Year", "Month", "Day", "Hour"]]
    )

    bicycle = bicycle.drop(columns=["Year", "Month", "Day", "Hour"])

    return bicycle.set_index("Date")


def commute():
    df = bicycle_timeseries()

    df = df.loc["2017-08-01":"2017-08-31"]

    df = df.groupby("Weekday").sum()

    df = df.reset_index()

    df["Weekday"] = df["Weekday"].replace({
        "Mon": 1,
        "Tue": 2,
        "Wed": 3,
        "Thu": 4,
        "Fri": 5,
        "Sat": 6,
        "Sun": 7
    })

    df = df.set_index("Weekday").sort_index()

    return df


def main():
    df = commute()

    ax = df.plot()

    ax.set_xticks([1, 2, 3, 4, 5, 6, 7])
    ax.set_xticklabels(
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    )

    plt.show()


if __name__ == "__main__":
    main()