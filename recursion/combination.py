"""
F(a) = a

F(ab) = a + F(b); b + F(a) = ab; ba

F(abc) = a + F(bc); b + F(ac); c + F(ab) = abc; acb; bac; bca; cab; cba

F(string) = for c in string: c + F(string - c)

"""


class Comb_1:
    def pai(self, t, k, n):
        """
        产生排列组合的递归写法
        :param t: 数组
        :param k: 起始排列值
        :param n: 数组长度
        :return:
        """
        if k == n - 1:  # 输出这个排列
            # for j in range(n):
            #     print(t[j], end ="")
            print(t)
            print()
        else:
            for i in range(k, n):
                t[i], t[k] = t[k], t[i]  # 一次挑选n个字母中的一个,和前位置替换
                self.pai(t, k + 1, n)  # 再对其余的n-1个字母一次挑选
                t[i], t[k] = t[k], t[i]  # 再换回来






def main_1():
    t = ["a", "b", "c"]
    k = 0
    n = 3
    Comb_1().pai(t, k, n)


class Comb:
    def comb(self, word):

        self.helper(word)


    def helper(self, word):
        if len(word) == 1:
            return word

        for i in word:
            rest = list(word[:])
            rest.remove(i)
            rest_comb = self.helper(rest)
            for p in rest_comb:
                print [i] + p
            # comb = word[i] + self.helper(rest, res)
                # if len(comb) == len(word):
                #     res.append(comb)


def main():
    sol = Comb()
    # words= ['', 'a', 'ab', 'abcd']
    # for word in words:
    #     print(word, sol.comb(word))
    print(sol.comb("abc"))


if __name__ == '__main__':
    main()
    # main_1()
