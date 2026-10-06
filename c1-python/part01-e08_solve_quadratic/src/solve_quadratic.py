import math

def solve_quadratic(a, b, c):
    x1=b*(-1)+ math.sqrt(b*b-4*a*c)
    x2=b*(-1)- math.sqrt(b*b-4*a*c)
    return (x1/(2*a),x2/(2*a))


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))

if __name__ == "__main__":
    main()
