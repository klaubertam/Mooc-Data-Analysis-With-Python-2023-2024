def find_matching(L, pattern):
    newlist=[]
    for i, x in enumerate(L):
        if pattern in x:
            newlist.append(i)
    return newlist

def main():
    pass

if __name__ == "__main__":
    main()
