# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:41:20 2018

@author: NickYue
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][i] += triangle[i-1][i-1]
        for i in range(2, len(triangle)):
            for j in range(1, len(triangle[i])-1):
                if triangle[i-1][j-1] < triangle[i-1][j]:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]
        return min(triangle[len(triangle)-1])
def printT(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end = ' ')
        print()
    print('-------')
def stringToInt2dArray(input):
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
            triangle = stringToInt2dArray(line)
            
            ret = Solution().minimumTotal(triangle)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
