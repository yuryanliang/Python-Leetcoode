"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""
class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c]=TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False
    def childSearch(self, word):
        cur  = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None
        return cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.childSearch(prefix) is not None

# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    word = 'ten'
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)