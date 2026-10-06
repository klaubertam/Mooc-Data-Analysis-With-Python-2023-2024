
import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    df=load()
    r,p= scipy.stats.pearsonr(df[:,0],df[:,2])
    return r

def correlations():
    df=load()
    return np.corrcoef(df, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
