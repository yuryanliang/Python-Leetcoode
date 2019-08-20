"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""
import sys
class Sol:
    def dist1(self, words, word1, word2):
        p1, p2, dist, i = -1, -1,sys.maxsize, 0
        is_same = (word1==word2)
        while i < len(words):
            if words[i] ==word1:
                if is_same and p1 >= 0:
                    dist = min(dist, i - p1)
                    p1 = i
            elif words[i]== word2:
                p2 = i
            if p1 >= 0 and p2 >= 0:
                dist = min(dist, abs(i - p1))
            i+=1


    def dist(self,words, word1, word2):
        pre_p1, p1, p2, dist, i= -1, -1, -1, sys.maxsize, 0

        while i < len(words):
            if words[i] == word1:
                pre_p1 = p1
                p1 = i
            elif words[i] == word2:
                p2 = i
            if word1 != word2 and p1 >= 0 and p2 >= 0:
                dist = min(dist, abs(p1 - p2))
            elif word1 == word2 and p1 >= 0 and pre_p1>=0:
                dist = min(dist, abs(p1 - pre_p1))
            i+=1
        return dist
if __name__ == '__main__':
    words = ["i", "a", "i", "b", "a"]
    word1 = "a"
    word2 = "a"
    print(Sol().dist(words, word1, word2))
