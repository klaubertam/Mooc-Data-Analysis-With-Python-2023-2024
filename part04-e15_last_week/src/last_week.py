import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    old = df[df["WoC"] > 1].copy()

    # Convert LW to numeric
    old["LW"] = pd.to_numeric(old["LW"], errors="coerce")

    # Remove songs where last week's position is unknown
    old = old.dropna(subset=["LW"])

    # Move song to last week's position
    old["Pos"] = old["LW"]

    # One less week on chart
    old["WoC"] = old["WoC"] - 1

    # We cannot reliably reconstruct these
    old["LW"] = np.nan
    old["Peak Pos"] = np.nan

    # Find missing positions
    existing_positions = set(old["Pos"].astype(int))
    missing_positions = set(range(1, 41)) - existing_positions

    missing = pd.DataFrame({"Pos": list(missing_positions)})

    for col in df.columns:
        if col not in missing.columns:
            missing[col] = np.nan

    result = pd.concat([old, missing], ignore_index=True)

    result = result.sort_values("Pos").reset_index(drop=True)

    return result


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()