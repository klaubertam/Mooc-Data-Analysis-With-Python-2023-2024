#!/usr/bin/env python3

def reverse_dictionary(d):
    newdic={}
    for key,value in d.items():
        if value[0] in newdic:
            newdic[value[0]].append(key)
        elif len(value)>1:
            for element in value:
                newdic[element]=[key]
        else:
            newdic[value[0]]=[]
            newdic[value[0]].append(key)
    return newdic

def main():
    pass

if __name__ == "__main__":
    main()
