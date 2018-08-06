# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:32:03 2018

@author: NickYue
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#先后将右子树和左子放入栈中，利用栈后入先出的原理遍历
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        res = []
        if root == None:
            return []
        queue.append(root)
        while (queue):
            cur_node = queue.pop()
            res.append(cur_node.val)            
            if cur_node.right :
                queue.append(cur_node.right)
            if cur_node.left :
                queue.append(cur_node.left)
        return res
