# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:38:49 2018

@author: NickYue
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__dp = [0] * len(nums)
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            self.__dp[i] = sums
        
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (i == 0):
            return self.__dp[j]
        else:
            return self.__dp[j] - self.__dp[i - 1]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    s = [-2, 0, 3, -1, 4, 5, -2, -2, 2]
    a = NumArray(s)
    print a.sumRange(0,6)