
def sum_equation(L):
    if len(L)==0:
        return "0 = 0"
    else:
        sentence=""
        sentence=" + ".join(map(str,L))
        return f"{sentence} = {sum(L)}"

def main():
    pass

if __name__ == "__main__":
    main()
