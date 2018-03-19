# Time:  O(logn)
# Space: O(1)

# Implement int sqrt(int x).
# 
# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
               if x < 2:
            return x
        
        left, right = 1, x
        while left <= right:
            mid = (left + right ) / 2
            if mid * mid > x :
                right = mid - 1
            else:
                left = mid + 1

        return right 


if __name__ == "__main__":
    print Solution().mySqrt(10)
