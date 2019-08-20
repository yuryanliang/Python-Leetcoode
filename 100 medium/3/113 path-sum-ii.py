"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

"""
DFS， 
init res, path, cur_sum
传入node target

如果到达底层， 看meet target 不
call left
call right

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Sol:
    def pathSum(self, root, sum) :
        target = sum
        res = []
        if not root:
            return []
        path = []
        path.append(root.val)
        cur_sum = 0
        cur_sum += root.val
        self.dfs(root, cur_sum, path, target, res)
        return res

    def dfs(self, node, cur_sum, path, target, res):
        if not node.left and not node.right:
            if target == cur_sum:
                res.append(path)

        if node.left:
            self.dfs(node.left, cur_sum + node.left.val, path + [node.left.val], target, res)

        if node.right:
            self.dfs(node.right, cur_sum + node.right.val, path + [node.right.val], target, res)

class Solution:

    def pathSum(self, root, sum) :
        def dfs(node, curr_sum, stack):
            if node.left is None and node.right is None:
                if sum == curr_sum:
                    return res.append(stack)

            if node.left:
                dfs(node.left, curr_sum + node.left.val, stack + [node.left.val])

            if node.right:
                dfs(node.right, curr_sum + node.right.val, stack + [node.right.val])

        res = []
        if not root:
            return []
        dfs(root, root.val, [root.val])

        return res

if __name__ == "__main__":
    root = TreeNode(5)

    print (Solution().pathSum(root, 5))