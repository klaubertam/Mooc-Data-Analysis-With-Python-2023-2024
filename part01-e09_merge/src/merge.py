def merge(L1, L2):
    L11=L1
    L22=L2
    thislist=L11+L22
    newlist=[]
    for i in range(len(thislist)):
        mini=min(thislist)
        newlist.append(mini)
        thislist.remove(mini)
    return newlist
def main():
    L1=[2, 3, 5, 7]
    L2=[1, 3, 6 , 6, 7]
    newlist=merge(L1,L2)
    print(newlist)

if __name__ == "__main__":
    main()
