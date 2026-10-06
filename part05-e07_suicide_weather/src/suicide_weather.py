
import pandas as pd

def suicide_fractions():
    df=pd.read_csv("src/who_suicide_statistics.csv",sep=",")
    df["fraction"]=df["suicides_no"]/df["population"]
    df=df.groupby("country")["fraction"].mean()
    return df

def suicide_weather():
    temp = pd.read_html(
        "src/List_of_countries_by_average_yearly_temperature.html",
        index_col=0,
        header=0
    )[0]

    col = "Average yearly temperature (1961–1990, degrees Celsius)"

    temp[col] = temp[col].str.replace("−", "-", regex=False)
    temp[col] = temp[col].astype(float)

    fractions = suicide_fractions()

    newdf = pd.merge(
        temp,
        fractions,
        left_index=True,
        right_index=True,
    )

    r = newdf["Average yearly temperature (1961–1990, degrees Celsius)"].corr(
        newdf["fraction"],
        method="spearman"
    )

    return (len(fractions), len(temp), len(newdf), r)


def main():
    a,b,c,r=suicide_weather()
    print(f"Suicide DataFrame has {a} rows")
    print(f"Temperature DataFrame has {b} rows")
    print(f"Common DataFrame has {c} rows")
    print(f"Spearman correlation: {r}")

if __name__ == "__main__":
    main()
