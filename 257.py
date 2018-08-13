# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:40:16 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(root,path,res):
            if root.left is None and root.right is None:
                res.append(path+str(root.val))
                return 
            if root.left:
                helper(root.left, path + str(root.val)+'->', res)
            if root.right:
                helper(root.right, path + str(root.val)+'->', res)

        if root is None:
            return []
        l = []
        helper(root, '', l)
        return l        