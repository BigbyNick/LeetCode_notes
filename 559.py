# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:11:43 2018

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
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        max_d = 0
        if root == None:
            return 0
        else:
            for child in root.children:
                c_depth = self.maxDepth(child)
                if max_d < c_depth:
                    max_d = c_depth
            max_d = max_d + 1
        return max_d