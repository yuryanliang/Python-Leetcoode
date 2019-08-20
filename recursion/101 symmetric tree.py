"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if (left and not right) or (right and not left) or (left.val != right.val):
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    print(Solution().isSymmetric(root))


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            l, r = stack.pop(), stack.pop()

            if not l and not r:
                continue
            if (not l and r) or (l and not r) or (l.val != r.val):
                return False

            stack.append(l.left)
            stack.append(r.right)

            stack.append(l.right)
            stack.append(r.left)
        return True


if __name__ == '__main__':
    main()
