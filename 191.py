# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 16:54:01 2018

@author: NickYue
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=bin(n)
        return n.count('1')

