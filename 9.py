# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:14:57 2018

@author: NickYue
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # pass 1
        # if (x < 0) or (x % 10 == 0 and x != 0):
        #     return False
        # y = x
        # x_ = 0
        # while y != 0 :
        #     x_ = x_ * 10 + y %10
        #     y = y / 10
        # return x_ == x
        
        # pass 2
        return str(x) == str(x)[::-1]
        