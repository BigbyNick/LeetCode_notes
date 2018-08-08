# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 00:02:51 2018

@author: NickYue
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[]
        for i in range(rowIndex+1):
            temp=[1]*(i+1)
            res.append(temp)
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res[rowIndex]