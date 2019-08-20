# vector < int > res(rowIndex + 1);
# res[0] = 1;
# for (int i = 1; i <= rowIndex; ++i) {
# for (int j = i; j >= 1; --j) {
# res[j] += res[j - 1];
# }
# }
# return res;


class Sol_1:
    def kth_row(self,k):
        res = []
        res.append(1)
        for i in range (1, k + 1):
            for j in range(i+1  ,0 ,-1 ):
                res[j]+=res[j-1]
        return res


def main():
    print(Sol_1().kth_row(3))


if __name__ == '__main__':
    main()
