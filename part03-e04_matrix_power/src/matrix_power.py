import numpy as np
from functools import reduce
def matrix_power(a, n):
    if n>0:
        return reduce(lambda x,y:x@y,(a for _ in range(n)))
    elif n==0:
        return np.eye(a.shape[1])
    else:
        a=np.linalg.inv(a)
        return reduce(lambda x,y:x@y, (a for _ in range(-n)))

def main():
    return

if __name__ == "__main__":
    main()
