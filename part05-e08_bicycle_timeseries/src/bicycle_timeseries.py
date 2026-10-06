
import pandas as pd

def bicycle_timeseries():
    bicycle=pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";").dropna(how="all").dropna(how="all",axis=1)
    newdf=bicycle["Päivämäärä"].str.split(expand=True).astype(object)
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
    newdf["Hour"] = newdf["Hour"].str[:2].astype(int)
    newdf["Day"] = newdf["Day"].astype(int)
    newdf["Month"] = newdf["Month"].astype(int)
    newdf["Year"] = newdf["Year"].astype(int)
    bicycle=pd.concat([bicycle,newdf],axis=1)
    bicycle= bicycle.drop(columns=["Päivämäärä"])
    bicycle["Date"]=pd.to_datetime(bicycle[["Year","Month","Day","Hour"]])
    bicycle=bicycle.drop(columns=["Year","Month","Day","Hour","Weekday"])
    return bicycle.set_index("Date")
def main():
    print(bicycle_timeseries())

if __name__ == "__main__":
    main()
