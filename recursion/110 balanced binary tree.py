"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        """
        而对于一颗树，它是一个平衡二叉树需要满足三个条件：
        它的左子树是平衡二叉树，它的右子树是平衡二叉树，它的左右子树的高度差不大于1。
        """
        if abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            return False
        res = self.isBalanced(root.left) and self.isBalanced(root.right)  # the res from next recursion
        return res

    def get_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))

# class Solution {
# public:
#     bool isBalanced(TreeNode *root) {
#         if (checkDepth(root) == -1) return false;
#         else return true;
#     }
#     int checkDepth(TreeNode *root) {
#         if (!root) return 0;
#         int left = checkDepth(root->left);
#         if (left == -1) return -1;
#         int right = checkDepth(root->right);
#         if (right == -1) return -1;
#         int diff = abs(left - right);
#         if (diff > 1) return -1;
#         else return 1 + max(left, right);
#     }
# };
