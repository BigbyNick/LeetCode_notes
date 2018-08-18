# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:45:51 2018

@author: NickYue
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        dp = [0] * n
        for i in range(2,n):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)

def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            A = stringToIntegerList(line)
            
            ret = Solution().numberOfArithmeticSlices(A)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()