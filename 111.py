# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 19:59:17 2018

@author: NickYue
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
        Ld = self.minDepth(root.left)
        Rd = self.minDepth(root.right)
        if Ld > Rd:
            return Rd + 1
        else:
            return Ld + 1
