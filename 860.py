# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 22:03:36 2018

@author: NickYue
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        tol_5 = 0
        tol_10 = 0
        tol_20 = 0
        flag = True
        n = len(bills)
        if n == 0:
            return True
        if n == 1 and bills[0] != 5:
            return False
        
        for i in range(n):
            if bills[i] == 5:
                tol_5 += 1
            if bills[i] == 10:
                if tol_5 > 0:
                    tol_5 -= 1
                    tol_10 += 1
                else:
                    flag = False
            if bills[i] == 20:
                if tol_10 > 0:
                    if tol_5 > 0:
                        tol_20 += 1
                        tol_10 -= 1
                        tol_5 -= 1
                    else:
                        flag = False
                else:
                    if tol_5 > 3:
                        tol_20 += 1
                        tol_5 -= 3
                    else:
                        flag = False
                    
        return flag

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            bills = stringToIntegerList(line)
            
            ret = Solution().lemonadeChange(bills)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()