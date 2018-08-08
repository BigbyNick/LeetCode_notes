# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 23:50:45 2018

@author: NickYue
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res=[]
        for i in range(numRows):
            temp=[1]*(i+1)
            res.append(temp)
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res        