"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorder(self, root) :
        res = []
        def helper(root, res):

            if not root:
                return
            res.append(root.val)
            helper(root.left, res)
            helper(root.right, res)
        helper(root, res)
        return res

class Sol:
    def preorder(self, root):
        res = []
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                res.append(p.val)
                p = p.left
            else:
                temp = stack.pop()
                p = temp.right
        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    result = Sol().preorder(root)
    print (result)