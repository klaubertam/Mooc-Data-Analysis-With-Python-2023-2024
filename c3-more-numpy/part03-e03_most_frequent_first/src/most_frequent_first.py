import numpy as np

def most_frequent_first(a, c):
    values, counts = np.unique(a[:, c], return_counts=True)
    frequencies = dict(zip(values, counts))
    row_frequencies = np.array([frequencies[x] for x in a[:, c]])
    return a[np.argsort(-row_frequencies)]

def main():
    pass

if __name__ == "__main__":
    main()
