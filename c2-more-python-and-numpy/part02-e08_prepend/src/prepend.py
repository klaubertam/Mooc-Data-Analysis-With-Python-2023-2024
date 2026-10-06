#!/usr/bin/env python3

class Prepend():
    def __init__(self,start:str):
        self.start=start
    def write(self,prepend:str):
        print(self.start+prepend)
    

def main():
    p=Prepend('+')
    p.write('hi')

if __name__ == "__main__":
    main()
