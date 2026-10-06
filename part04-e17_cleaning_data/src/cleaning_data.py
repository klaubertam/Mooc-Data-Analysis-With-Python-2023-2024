#!/usr/bin/env python3

import pandas as pd
import numpy as np


import pandas as pd
import numpy as np

def cleaning_data():

    df = pd.read_csv("src/presidents.tsv", sep="\t")

    def fix_name(x):
        if "," in x:
            last, first = x.split(",")
            return first.strip().title() + " " + last.strip().title()
        return x.title()

    df["President"] = df["President"].apply(fix_name)
    df["Vice-president"] = df["Vice-president"].apply(fix_name)

    df["Start"] = df["Start"].str.replace(" Jan", "").astype(int)

    df["Last"] = df["Last"].replace("-", np.nan).astype(float)

    df["Seasons"] = df["Seasons"].replace("two", 2).astype(int)

    df["President"] = df["President"].astype(object)
    df["Vice-president"] = df["Vice-president"].astype(object)

    return df
def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
