#!/usr/bin/env python3

import numpy as np

def diamond(n):
    eye = np.eye(n, dtype=int)

    # top half
    top = np.concatenate((eye[::-1], eye[:, 1:]), axis=1)

    # bottom half
    bottom = top[::-1][1:]

    return np.concatenate((top, bottom), axis=0)

def main():
    pass

if __name__ == "__main__":
    main()
