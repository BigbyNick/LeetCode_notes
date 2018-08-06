# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 23:07:35 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def grow_tree_by_poiANDin(self, s_poi, s_in):
        if len(s_poi) == 0:
            return None
        root = s_poi[0]
        root_index = s_in.index(s_poi[0])
        root_node = TreeNode(root)
        root_node.left = self.grow_tree_by_poiANDin(s_poi[1:root_index + 1],s_in[0:root_index])
        root_node.right = self.grow_tree_by_poiANDin(s_poi[root_index + 1:],s_in[root_index + 1 :])
        return root_node
    
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return ( self.grow_tree_by_poiANDin(preorder,inorder) )