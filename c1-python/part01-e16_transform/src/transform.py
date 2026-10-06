def transform(s1, s2):
    L1 = list(map(int, s1.split()))
    L2 = list(map(int, s2.split()))

    newlist = zip(L1, L2)
    newerlist = []
    for a,b in newlist:
        newerlist.append(a*b)
    return newerlist
    
def main():
    pass

if __name__ == "__main__":
    main()
