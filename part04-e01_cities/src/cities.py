#!/usr/bin/env python3

import pandas as pd

def cities():
    names=["Helsinki","Espoo","Tampere","Vantaa","Oulu"]
    s1=pd.Series([643272,279044,231853,223027,201810],index=names)
    s2=pd.Series([715.48,528.03,689.59,240.35,3817.52],index=names)
    return pd.DataFrame({"Population":s1,"Total area":s2})
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
