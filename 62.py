# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:02:09 2018

@author: NickYue
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:19:01 2018

@author: NickYue
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 and n == 0:
            return None
        cost = [([0] * n) for i in range(m)]
        for i in range(m):
            cost[i][0] = 1

        for i in range(n):
            cost[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                cost[i][j] = cost[i-1][j] + cost[i][j-1]

        return cost[m-1][n-1]

def stringToInt(input):
    return int(input)

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
            m = stringToInt(line)
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().uniquePaths(m, n)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()