class Factorial:
    def factorial(self,n):
        """
        5! = 5 * 4 * 3 *2 * 1
            = 5 * 4!
        4! = 4 * 3 * 2 * 1
            = 4 * 3!


        res = n * factorial(n -1) if n > 0
        res = 1 if n = 0

        :param n:
        :return:
        """
        if  n == 0:
            return 1

        next_one = self.factorial(n - 1)
        res = n * next_one
        return res
def main_1():
    res = Factorial().factorial(5)
    print(res)


if __name__ == '__main__':
    main_1()
