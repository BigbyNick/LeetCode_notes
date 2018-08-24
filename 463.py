# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:48:45 2018

@author: NickYue
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tol = 0
        recount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    tol += 1
                    if (i>0) and (grid[i-1][j] == 1):
                        recount += 1
                    if (i<len(grid)-1) and (grid[i+1][j] == 1):
                        recount += 1
                    if (j>0) and (grid[i][j-1] == 1):
                        recount += 1
                    if (j<len(grid[i])-1) and (grid[i][j+1] == 1):
                        recount += 1
        return 4*tol-recount

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
            grid = stringToInt2dArray(line)
            
            ret = Solution().islandPerimeter(grid)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()