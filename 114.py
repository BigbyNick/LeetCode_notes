# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 23:03:40 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

post_l = []
class Solution(object):
    
       
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        Node = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = Node
