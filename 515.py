# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:01:53 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes = [root]
        res = []
        if not root :
            return []
        while nodes:
            templist = []
            len_list = len(nodes)
            for i in range( len_list ):
                cur_node = nodes.pop(0)
                templist.append(cur_node.val)
                if cur_node.left:
                    nodes.append(cur_node.left)
                if cur_node.right:
                    nodes.append(cur_node.right)
            res.append(templist)  
        return res

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = self.levelOrder(root)     
        res2 = []
        for ele in res:
            res2.append(max(ele))
        return res2