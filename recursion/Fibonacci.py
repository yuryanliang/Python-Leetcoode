"""
F(1) = 1 if n = 1
F(2) = 1 + 2 = 3 if n = 2
F(3) = F(1) + F(2) = 1 + 3 = 4
F(4) = F(2) + F(3) = 3 + 4 = 7
F(n) = F(n - 2) + F(n - 1) if n > 2

"""

class Fabonacci:
    def F(self, x):
        if x == 1:
            return 1
        elif x == 2:
            return 3
        res = self.F(x - 2) + self.F(x - 1)
        return res
def main():
    x = 5
    res = Fabonacci().F(x)
    print(res)


if __name__ == '__main__':
    main()
