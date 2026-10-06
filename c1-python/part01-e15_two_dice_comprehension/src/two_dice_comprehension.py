def main():
    s={ (i,j):i+j==5 for i in range(1,7) for j in range(1,7)}
    print(s)

if __name__ == "__main__":
    main()


def main():
    for i in range(1,7):
        for j in range(1,7):
            if i+j==5:
                pair=(i,j)
                print(pair)

if __name__ == "__main__":
    main()
