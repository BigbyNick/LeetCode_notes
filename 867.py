# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 23:47:56 2018

@author: NickYue
"""

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(A), len(A[0])
        res = [[0] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                res[col][row] = A[row][col]
        return res        