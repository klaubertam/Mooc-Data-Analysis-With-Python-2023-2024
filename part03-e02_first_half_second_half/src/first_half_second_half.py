import numpy as np

def first_half_second_half(a):
    return a[np.sum(a[:,:a.shape[1]//2],axis=1)>np.sum(a[:,a.shape[1]//2:],axis=1)]

def main():
    pass

if __name__ == "__main__":
    main()
