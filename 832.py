# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:48:22 2018

@author: NickYue
"""

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = 1-int(A[i][j])
            A[i] = A[i][::-1]
        return A