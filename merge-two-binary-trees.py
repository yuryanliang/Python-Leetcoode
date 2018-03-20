Skip to content
This repository
Search
Pull requests
Issues
Marketplace
Explore
 @yuryanliang
Sign out
0
0 1,618 yuryanliang/LeetCode
forked from kamyu104/LeetCode
 Code  Pull requests 0  Projects 0  Wiki  Insights  Settings
LeetCode/Python/merge-two-binary-trees.py
c5e598a  on Jul 18, 2017
@swaroopgrs swaroopgrs Update merge-two-binary-trees.py
@kamyu104 @swaroopgrs
     
54 lines (50 sloc)  1.53 KB
# Time:  O(n)
# Space: O(h)

# Given two binary trees and imagine that 
# when you put one of them to cover the other,
# some nodes of the two trees are overlapped
# while the others are not.
#
# You need to merge them into a new binary tree.
# The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#       /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
#	 
# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
思路
合并两个二叉树当然就是同步遍历了，对于相同位置上的一对结点n1和n2，处理策略是：

若n1和n2都存在，则只需要保留其中一个结点（如n1），将另一结点的值加到此结点上即可（如n1.val += n2.val）。
若n1或n2任一不存在，则合并后的二叉树对应位置上的结点就是存在的那个了。
若n1和n2都不存在，则合并后仍不存在。
所以我们可以假定第一颗树为“主树”，第二颗树为“从树”：碰到对应位置上“主树”结点存在且“从树”结点存在，则将“从树”结点值加到“主树”；碰到对应位置上“主树”结点存在而“从树”结点不存在，则不作任何处理；碰到对应位置上“主树”结点不存在而“从树”结点存在，则将“从树”结点移到“主树”对应位置下。

因为涉及到结点的更新，所以用递归会是一个简单而又方便的方法。
