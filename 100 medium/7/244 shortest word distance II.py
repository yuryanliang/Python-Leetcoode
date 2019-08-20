"""
This is a follow up of Shortest Word Distance.
The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters.
 How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
from collections import defaultdict
import sys


class Sol:
    def __init__(self, words):
        self.words = words
        self.lookup = defaultdict(list)
        for i, val in enumerate(self.words):
            self.lookup[val].append(i)

    def dist1(self, word1, word2):
        dist = sys.maxsize
        index1 = self.lookup[word1]
        index2 = self.lookup[word2]

        i, j = 0, 0
        while i < len(index1) and j < len(index2):
            dist = min(dist, abs(index1[i] - index2[j]))
            if index1[i] < index2[j]:
                i += 1
            else:
                j += 1

    def dist(self, word1, word2):
        # print(self.lookup)
        dist = sys.maxsize
        index1 = self.lookup[word1]
        index2 = self.lookup[word2]
        for i in index1:
            for j in index2:
                dist = min(dist, abs(i -j))
        return dist

class Sol:
    def __init__(self, words):
        self.words = words
        self.lookup = defaultdict(list)
        for i, val in enumerate(self.words):
            self.lookup[val].append(i)
    def dist1(self, word1, word2):
        dist = sys.maxsize
        index1= self.lookup[word1]
        index2 = self.lookup[word2]

        i, j = 0, 0
        while i < len(index1) and j < len(index2):
            dist = min(dist, abs(index1[i] - index2[j]))
            if index1[i] < index2[j]:
                i += 1
            else:
                j += 1





if __name__ == '__main__':
    words = ["i", "a", "i", "b", "a"]
    word1 = "a"
    word2 = "b"
    print(Sol(words).dist1(word1, word2))

