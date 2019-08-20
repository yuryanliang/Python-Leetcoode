"""
F(1) = 1

F(12) = 2 + F(1) = 2 1

F(123) = 3 + F(12) = 3 2 1

F(1234) = 4 F(123) = 4 3 2 1

F(n) = n if len(n) == 1
F(n) = n % 10 + F(n // 10) if n len(n) >1

"""

class Reverse_1:
    def rev(self, x):
        if len(str(x)) == 1:
            return x
        else:
            res = str(x % 10) + str(self.rev(x // 10))
            return int(res)

def main_1():
    x = 1234
    res = Reverse_1().rev(x)
    print(res)

class Reverse_2:

    def rev(self, x):
        print(x % 10)
        if x > 10:
            self.rev(x // 10)

def main_2():
    x = 1234
    res = Reverse_2().rev(x)
    print(res)

if __name__ == '__main__':
    # main_1()
    main_2()
