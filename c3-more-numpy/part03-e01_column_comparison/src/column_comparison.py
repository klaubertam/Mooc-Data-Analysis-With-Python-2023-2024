import numpy as np

def column_comparison(array):
    return array[array[:, 1] > array[:, -2]]

def main():
    arr = np.array([
        [8, 9, 3, 8, 8],
        [0, 5, 3, 9, 9],
        [5, 7, 6, 0, 4],
        [7, 8, 1, 6, 2],
        [2, 1, 3, 5, 8]
    ])

    result = column_comparison(arr)
    print(result)

if __name__ == "__main__":
    main()
