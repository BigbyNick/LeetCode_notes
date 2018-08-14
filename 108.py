# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 23:02:37 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root = TreeNode(nums[len(nums)//2])
        root.left = self.sortedArrayToBST(nums[:len(nums)//2])
        root.right = self.sortedArrayToBST(nums[len(nums)//2 + 1:])
        return root