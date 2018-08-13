# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:16:01 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def dfs(root,sum):
            if root==None:
                return 0
            if root.val==sum:
                return 1+dfs(root.left,0)+dfs(root.right,0)
            return dfs(root.left,sum-root.val)+dfs(root.right,sum-root.val)
        if root==None:
            return 0
        return dfs(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)