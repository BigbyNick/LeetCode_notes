# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:57:32 2018

@author: NickYue
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None :
            return []
        res.append(root.val)

        for child in root.children:
            res = res + self.preorder(child)  
        return res