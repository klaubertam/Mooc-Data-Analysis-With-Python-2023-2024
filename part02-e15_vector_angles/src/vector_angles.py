#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    X=np.array(X)
    Y=np.array(Y)
    inner_product=np.sum((X*Y),axis=1)
    return np.degrees(np.arccos(np.clip(inner_product/(np.sqrt(np.sum((X*X),axis=1)) * np.sqrt(np.sum((Y*Y),axis=1))),-1,1)))
def main():
    X=[[1],
       [2],
       [3]]
    Y=[[2],
       [3],
       [4]]
    print(vector_angles(X,Y))

if __name__ == "__main__":
    main()
