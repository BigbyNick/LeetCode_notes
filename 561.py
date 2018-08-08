# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 23:49:27 2018

@author: NickYue
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])         