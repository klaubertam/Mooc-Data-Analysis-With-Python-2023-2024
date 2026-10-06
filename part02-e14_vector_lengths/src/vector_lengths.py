#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt((a**2).sum(axis=1))

def main():
    a=np.array([[3,4],[5,12],[8,15]])
    print(vector_lengths(a))
if __name__ == "__main__":
    main()
