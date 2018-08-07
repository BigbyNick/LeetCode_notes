# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 23:12:33 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.temp = 0
        
        def depth(p):
            if not p:
                return 0#bottom of the tree
            left,right = depth(p.left),depth(p.right)
            self.temp = max(self.temp,left+right)
            return 1+max(left,right)
        
        depth(root)
        
        return self.temp        