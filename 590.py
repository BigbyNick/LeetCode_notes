# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 00:10:33 2018

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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None :
            return []
        for child in root.children:
            res = res + self.postorder(child)
        res.append(root.val)
        return res