#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    return ((a.shape[0]-1)/2,(a.shape[1]-1)/2)

def radial_distance(a):
    cy, cx = center(a)
    y, x = np.meshgrid(
        np.arange(a.shape[0]),
        np.arange(a.shape[1]),
        indexing="ij"
    )
    return np.sqrt((y - cy)**2 + (x - cx)**2)

def scale(a, tmin=0.0, tmax=1.0):
    amin = np.min(a)
    amax = np.max(a)

    if amin == amax:
        return np.full_like(a, tmin)

    return tmin + (a - amin) * (tmax - tmin) / (amax - amin)

def radial_mask(a):
    distances = radial_distance(a)

    if np.max(distances) == 0:
        return np.ones(distances.shape)

    return 1 - scale(distances)

def radial_fade(a):
    return a * radial_mask(a)[..., np.newaxis]

def main():
    a = plt.imread("src/painting.png")
    fig,ax=plt.subplots(3,1)
    ax[0].imshow(a)
    ax[1].imshow(radial_mask(a))
    ax[2].imshow(radial_fade(a))
    plt.show()

if __name__ == "__main__":
    main()
