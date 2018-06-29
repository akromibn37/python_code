class Complex :
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        out= ''
        if self.a == 0 and self.b == 0 :
            return '0'
        if self.a != 0:
            out = str(self.a)
        if self.b != 0:
            if self.a != 0 and self.b > 0: out += "+"
            if self.b < 0: out += "-"
            x = abs(self.b)
            if x == 1:
                out += "i"
            else:
                out += str(x)+"i"
        return out

    def __add__(self, rhs):
        return Complex(self.a+rhs.a, self.b+rhs.b)
    def __mul__(self, rhs):
        return Complex(self.a*rhs.a-self.b*rhs.b,self.a*rhs.b+self.b*rhs.a)
    def __truediv__(self, rhs):
        x = rhs.a**2+rhs.b**2
        return Complex((self.a*rhs.a+self.b*rhs.b)/x, (-self.a*rhs.b+self.b*rhs.a)/x)

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)
