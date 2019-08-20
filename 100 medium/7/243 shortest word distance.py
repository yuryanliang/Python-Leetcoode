"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list
"""
import sys


class Sol:
    def distance(self, words, word1, word2):
        last_w1 = -1
        last_w2 = -1
        j = 0
        dist = sys.maxsize
        while j < len(words):
            if words[j] == word1:
                last_w1 = j
            elif words[j] == word2:
                last_w2 = j
            if last_w1 >= 0 and last_w2 >= 0:
                dist = min(dist, abs(last_w1 - last_w2))
            j += 1
        return dist

    def distance(self, words, word1, word2):
        last_w1 = -1
        last_w2 = -1
        j = 0
        dist = sys.maxsize

        while j < len(words):
            if words[j]== word1:
                last_w1 = j
            elif words[j] == word2:
                last_w2 = j
            if last_w1 >= 0 and last_w2 >= 0:
                dist = min(dist, abs(last_w1 - last_w2))
            j +=1
        return dist


if __name__ == '__main__':
    words = ["i", "a", "i", "b", "a"]
    word1 = "a"
    word2 = "b"
    print(Sol().distance(words, word1, word2))
