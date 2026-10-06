#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    l = {
        "State": ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"],
        "Year of independence": ["-", 1917, 1776, 1523, "-", 1992],
        "President": ["-", "Niinistö", "Trump", "-", "Steinmeier", "Putin"]
    }

    df = pd.DataFrame(l).set_index("State")

    df["Year of independence"] = df["Year of independence"].replace("-", np.nan)
    df["Year of independence"] = df["Year of independence"].astype(float)

    df["President"] = df["President"].replace("-", np.nan)

    return df   
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
