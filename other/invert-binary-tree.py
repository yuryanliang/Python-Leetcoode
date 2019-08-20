226. Invert Binary Tree [easy] (Python)
原创 2016年05月12日 14:36:34 标签：python /LeetCode 1354
题目链接
https://leetcode.com/problems/invert-binary-tree/

题目原文
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
1
2
3
4
5
to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
1
2
3
4
5
Trivia: 
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

题目翻译
翻转二叉树。

花絮： 
Max Howell 在 tweet 中说： 
谷歌：虽然我们的工程师中有90%的人在用你写的软件，但你居然不能再白板上写个翻转二叉树的代码，滚吧。

思路方法
思路一
（DFS）递归算法，每次递归交换当前节点的左右子树，同时对左右子树做同样的处理。

代码一

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
既然这（可能）是一道谷歌的面试题，我们要尝试写出不同的代码来应付可能的题目限制，比如不准用递归，那我们用栈好了。。。

代码二

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root

        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
思路二
（BFS）除了上面的用栈的解法，用队列也可以解决该问题。先将根节点入队，交换左右节点并将非空的节点加入队列，再将根节点出队，这样循环下去即可。

代码

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        q = [root]
        while len(q) != 0:
            q[0].left, q[0].right = q[0].right, q[0].left
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            del q[0]

        return root
