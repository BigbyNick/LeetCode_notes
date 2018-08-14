# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 00:06:21 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, b, e):#b,e为开始和结束数字
        if b > e:
            return [None]
        res = []
        for rootVal in range(b, e + 1):
            leftTree = self.dfs(b, rootVal - 1)
            rightTree = self.dfs(rootVal + 1, e)
            for i in leftTree:
                for j in rightTree:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0:
            return []
        return self.dfs(1,n)
        