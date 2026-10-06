#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    img = img.astype(float)
    gray=(0.2126*img[:,:,0]+0.7152*img[:,:,1]+0.0722*img[:,:,2])
    return gray
def to_red(img):
    img2=img.copy()
    img2[:,:,1]=0
    img2[:,:,2]=0
    return img2
def to_green(img):
    img2=img.copy()
    img2[:,:,0]=0
    img2[:,:,2]=0
    return img2
def to_blue(img):
    img2=img.copy()
    img2[:,:,0]=0
    img2[:,:,1]=0
    return img2
def main():
    img = plt.imread("src/painting.png")
    gray=to_grayscale(img)
    plt.gray()
    plt.imshow(gray)
    plt.show()

    fig,ax=plt.subplots(3,1)
    ax[0].imshow(to_red(img))
    ax[0].set_title("Red")
    ax[1].imshow(to_green(img))
    ax[1].set_title("Green")
    ax[2].imshow(to_blue(img))
    ax[2].set_title("Blue")
    plt.show()

if __name__ == "__main__":
    main()
