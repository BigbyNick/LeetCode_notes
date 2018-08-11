# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:20:06 2018

@author: NickYue
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = ""
        for i in range(num // 1000):
            str += 'M'
        num = num % 1000
        x = num // 100
        if x == 0:
            pass        
        elif x < 4:
            for i in range(x):
                str += 'C'
        elif x == 4:
            str += 'CD'
        elif x == 5:
            str += 'D'
        elif x < 9:
            str += 'D'
            for i in range(x-5):
                str += 'C'
        else:
            str += 'CM'

        num = num % 100
        x = num // 10
        if x == 0:
            pass        
        elif x < 4:
            for i in range(x):
                str += 'X'
        elif x == 4:
            str += 'XL'
        elif x == 5:
            str += 'L'
        elif x < 9:
            str += 'L'
            for i in range(x-5):
                str += 'X'
        else:
            str += 'XC'

        num = num % 10
        x = num 
        if x == 0:
            pass        
        elif x < 4:
            for i in range(x):
                str += 'I'
        elif x == 4:
            str += 'IV'
        elif x == 5:
            str += 'V'
        elif x < 9:
            str += 'V'
            for i in range(x-5):
                str += 'I'
        else:
            str += 'IX'

        return str

#    
#if __name__ == '__main__':
##    s = [1, 2, 3, -1, -1, -1, 4, -1, -1]
#    a = 4
#    print (intToRoman(a))
#    b = 9
#    print (intToRoman(b))
#    c = 58
#    print (intToRoman(c))
#    d = 1994
#    print (intToRoman(d))
