import math

def main():
    while True:
        shape=input("Choose a shape (triangle, rectangle, circle): ")
        if shape=="triangle":
            base=int(input("Give base of the triangle: "))
            height=int(input("Give height of the triangle: "))
            print(f"The area is {base*height/2}")
        elif shape=="rectangle":
            width=int(input("Give width of the triangle: "))
            height=int(input("Give height of the triangle: "))
            print(f"The area is {float(base*height)}")
        elif shape=="circle":
            radius=int(input("Give radius of the triangle: "))
            print(f"The area is {math.pi*radius*radius}")
        elif not shape:
            break
        else:
            print("Unknown shape!")
        

if __name__ == "__main__":
    main()
