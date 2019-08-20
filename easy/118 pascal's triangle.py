class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        pt = [[1]]

        for i in range(1, numRows):
            pt_mid = []
            for j in range(0, i - 1):
                val = pt[i - 1][j] + pt[i - 1][j + 1]
                pt_mid.append(val)
            pt_row = [1] + pt_mid + [1]
            pt.append(pt_row)
        return pt

def main():
    print(Solution().generate(5))
    print(Solution().generate(0))

class Sol_1:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i + 1):
                res[i].append((res[i - 1][j - 1] if j > 0 else 0) + (res[i - 1][j] if j < i else 0))
        return res
def main_1():
    print(Solution().generate(5))
    print(Solution().generate(0))

if __name__ == '__main__':
    # main()
    main_1()
