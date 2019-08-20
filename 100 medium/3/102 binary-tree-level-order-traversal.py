"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

"""
用deque 结构

先把root 压入，
while q 的循环
popleft， 放入res/， 压入left， 压入right
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        if self:
            return "{} <- {} -> {}".format(repr(self.left), self.val, repr(self.right))
class Sol:
    def levelOrder(self, root):
        from collections import deque #deque.pop, deque.popleft, deque.append
        q = deque()
        q.append(root)
        res = []
        while q:
            node =q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res



class Solution:
    def levelOrder(self, root):
        """
        1. 初始化队列，将头节点保存，由于题目需要根据节点所在的层返回，所以这里队列中的每一项都是一个tuple(节点，层级)，头结点的tuple是（root, 0）
        2. 不断的出队列，知道队列为空，整个树就被遍历完了。
        3.  从队列中获取到当前节点，和节点所在的层级，如果节点是空的就继续出队列，否则进行步骤4和5。
        4.  如果当前的层级是第一次出现，则将结果集中存入一个list，供当前层级存放节点的值。这里使用一个set来判断层级是否是第一次出现，当然还可以使用（len(结果集) - 1 != level ）这种方式，但是不太语义化，本文就没有采取。
        5. 将节点的值存入结果集中对应位置的list中，将左节点，右节点加入队列
        """
        # 步骤1
        from collections import deque
        node_queue = deque()
        node_queue.append((root, 0))

        res, res_set = [], set()

        # 步骤2
        while node_queue:
            # 步骤三
            node, level = node_queue.popleft()
            if node:
                # 步骤四
                if level not in res_set:
                    res_set.add(level)
                    res.append([])
                # 步骤五
                res[level].append(node.val)
                node_queue.append((node.left, level + 1))
                node_queue.append((node.right, level + 1))

        return res
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    result = Solution().levelOrder(root)
    print (result)