# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:31:08 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def grow_tree_by_inANDpost(self, s_in, s_post):
        if len(s_post) == 0:
            return None
        if len(s_post) == 1:
            return TreeNode(s_in[0])
        
        root = s_post[len(s_post)-1]
        
        root_node = TreeNode(s_post[len(s_post)-1])
        root_index = s_in.index(s_post[len(s_post)-1])
        root_node.left = self.grow_tree_by_inANDpost(s_in[0:root_index], s_post[0:root_index])
        root_node.right = self.grow_tree_by_inANDpost(s_in[root_index + 1 :], s_post[root_index: len(s_post) - 1])
        return root_node

    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return ( self.grow_tree_by_inANDpost(inorder, postorder) )