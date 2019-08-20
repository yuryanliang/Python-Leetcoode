import operator
class Prefix:
    def eva(self, s):
        array = s.split(" ")
        return self.helper(array)

    def helper(self, array):
        operators = ["+", "-", "*", "/"]
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}

        if len(array) == 1:
            return int(array[0])
        elif len(array) == 3:
            return ops[array[0]](int(array[1]), int(array[2]))
        if array[-3] in operators:
            first = array[1:len(array) - 3]
            second = array[-3:]
            return ops[array[0]](self.helper(first), self.helper(second))
        if array[-4] in operators:
            first = array[1:len(array) - 1]
            second = array[-1]
            return ops[array[0]](self.helper(first), int(second))


def main():
    # s = "+ 2 1"
    # s = "* + 3 2 2"
    # s = (4 + 2) / (1 + 1) # = 3 = / + 4 2 + 1 1
    # s = (1 + 2) * (3 + 4) + 7
    s = "+ * + 1 2 + 3 4 7"
    # s ="* + 1 2 + 1 1"
    ans = Prefix().eva(s)
    print(ans)

if __name__ == '__main__':
    main()
