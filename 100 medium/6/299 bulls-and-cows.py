"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""


# https://leetcode.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret, guess):
        bull = 0
        cow = 0
        lookup ={}
        for i, val in enumerate(secret):
            if val == guess[i]:
                bull +=1
            else:
                lookup[val] =lookup.get(val, 0)+1
        for i, val in enumerate(secret):
            if val != guess[i] and lookup.get(guess[i], 0)!=0:
                cow +=1
                lookup[guess[i]]-=1
        return str(bull)+"A"+str(cow)+"B"

    def get(self, secret, guess):
        bull = 0
        cow = 0
        lookup = {}

        for i, val in enumerate(secret):
            if val == guess[i]:
                bull +=1
            else:
                lookup[val]=lookup.get(val, 0) + 1

        for i, val in enumerate(secret):
            if val != guess[i] and lookup.get(guess[i], 0)!=0:
                cow +=1
                lookup[guess[i]]-=1

        return str(bull)+"A"+str(cow)+"B"

class Solution:
    def getHint(self, secret, guess):

        d = {}
        bull, cow = 0, 0

        for index, s in enumerate(secret):
            if guess[index] == s:
                bull += 1
            else:
                d[s] = d.get(s, 0) + 1

        for index, s in enumerate(secret):
            if (guess[index] != s) & (d.get(guess[index], 0) != 0):
                cow += 1
                d[guess[index]] -= 1

        return str(bull) + "A" + str(cow) + "B"


if __name__ == '__main__':
    # secret = "1807"
    # guess = "7810"
    secret = "1123"
    guess = "0111"
    print(Solution().getHint(secret, guess))
