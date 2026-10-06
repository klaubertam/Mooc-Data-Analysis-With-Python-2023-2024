def triple(num:int):
    return 3*num

def square(num:int):
    return num*num

def main():
    for i in range(1,11):
        sqr=square(i)
        trp=triple(i)
        if sqr>trp:
            break
        else:
            print(f"triple({i})=={trp} square({i})=={sqr}")

if __name__ == "__main__":
    main()
