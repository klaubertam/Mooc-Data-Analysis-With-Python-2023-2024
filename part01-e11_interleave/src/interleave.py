def interleave(*lists):
    thislist= list(zip(*lists))
    newlist=[]
    for parts in thislist:
        for part in parts:
            newlist.append(part)
    return newlist


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
