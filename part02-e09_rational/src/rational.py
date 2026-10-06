from fractions import Fraction

class Rational:
    def __init__(self, n: int, m: int):
        self.r = Fraction(n, m)

    def __add__(self, other):
        result = self.r + other.r
        return Rational(result.numerator, result.denominator)

    def __sub__(self, other):
        result = self.r - other.r
        return Rational(result.numerator, result.denominator)

    def __mul__(self, other):
        result = self.r * other.r
        return Rational(result.numerator, result.denominator)

    def __truediv__(self, other):
        result = self.r / other.r
        return Rational(result.numerator, result.denominator)

    def __gt__(self, other):
        return self.r > other.r

    def __lt__(self, other):
        return self.r < other.r

    def __eq__(self, other):
        return self.r == other.r

    def __str__(self):
        return str(self.r)
    

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
