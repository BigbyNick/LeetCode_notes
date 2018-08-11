# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:03:52 2018

@author: NickYue
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        res = re.findall(r"^[\+\-]?\d+",str.strip())
        print(res)
        if res !=[]:
            if int(res[0]) > (2**31-1):
                return (2**31-1)
            if int(res[0]) < (-2**31):
                return (-2**31)
            return int(res[0])
        else:
            return 0