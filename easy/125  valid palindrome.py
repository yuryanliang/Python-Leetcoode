"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
class Sol_1:
    def isPalindrome(self, s):
        temp=''
        for c in s:
            if c.isalpha() or c.isdigit():
                temp += c
        n = len(s)
        temp = temp.lower()
        return temp == temp[::-1]


def main_1():
    s ="A man, a plan, a canal: Panama"
    print(Sol_1().isPalindrome(s))


if __name__ == '__main__':
    main_1()




class Solution(object):
    def isPalindrome(self, s):

        if not s:
            return True

        end = len(s) - 1

        if (end == 0):
            return True

        l = 0
        r = end

        while (l < r):
            if (not s[l].isalnum()):
                l += 1
                continue

            if (not s[r].isalnum()):
                r -= 1
                continue

            if (s[l].lower() != s[r].lower()):
                return False
            else:
                l += 1
                r -= 1

        return True


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        allowed = set(string.ascii_lowercase + string.digits)
        s = [c for c in s.lower() if c in allowed]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

class Solution:
	def isPalindrome(self, s: str) -> bool:
		s = s.lower()
		res = ""
		for i in s:
			if i.isalpha() or i.isdigit():
				res += i
		return res == res[::-1]