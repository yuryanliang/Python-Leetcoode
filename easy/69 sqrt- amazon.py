# brute force
class Sol_1:
    def sqrt_1(self, n): # n = 7
        if n < 0:
            return -1

        # find the sqrt
        i = 0
        while i ** 2 < n: # i = 2
            i+=1
        i = i - 1

        # choose the close one
        small = i ** 2
        large = (i + 1 ) ** 2
        if abs(small - n) < abs(large - n):
            return i
        else:
            return i + 1

def main_1():
    nums = [-1, 1, 5, 7]
    for i in nums:
        print(Sol_1().sqrt_1(i))

# binary search
class Sol_2:
    def sqrt_2(self, n): # n = 7
        if n < 0:
            return -1

        left = 0
        right = n

        while left < right: # i = 2
            mid = (left + right) // 2
            if mid ** 2 < n:
                left = mid + 1
            else:
                right = mid
        i = left -1 # left is the first one >= n, so left - 1

        small = i ** 2
        large = (i + 1 ) ** 2

        if abs(small - n) < abs(large - n):
            return i
        else:
            return i + 1

def main_2():
    nums = [-1 , 1,5, 7]
    for i in nums:
        print(Sol_2().sqrt_2(i))


if __name__ == '__main__':
    # main_1()
    main_2()
