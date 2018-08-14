# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 00:34:10 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        que = [root]
        res = []
        if root == None:
            return []
        while que :
            sum_que = 0
            len_que = len(que)
            for i in range(len_que):
                cur_node = que.pop(0)
                sum_que += cur_node.val
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
            res.append(1. * sum_que / len_que)
        return res
            