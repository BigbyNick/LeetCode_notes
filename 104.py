# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:19:06 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            Ldepth = self.maxDepth(root.left)
            Rdepth = self.maxDepth(root.right)
        if Ldepth > Rdepth:
            return Ldepth + 1
        else:
            return Rdepth + 1
        