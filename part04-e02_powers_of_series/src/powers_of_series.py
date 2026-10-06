#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    return pd.DataFrame({i: s**i for i in range(1, k+1)})


def main():
    s = pd.Series([1, 2, 3, 4, 5], index=(0, 1, 2, 3, 4))
    print(powers_of_series(s, 5))


if __name__ == "__main__":
    main()