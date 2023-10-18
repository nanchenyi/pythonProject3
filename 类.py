class Rational0:
    pass
    def __init__(self, num, den=1):
        self.num = num
        self.den = den
    def plus(self, another):
        den = self.den * another.den
        num = (self.num * another.den + self.den * another.num)
        return Rational0(num, den)
    def __add__(self, another):
        den = self.den * another.den
        num = (self.num * another.den + self.den * another.num)
        return Rational0(num, den)
