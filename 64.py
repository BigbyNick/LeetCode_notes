# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:19:01 2018

@author: NickYue
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None:
            return None
        row = len(grid)
        col = len(grid[0])
        cost = [([0] * col) for i in range(row)]
        cost[0][0] = grid[0][0]

        for i in range(1,row):
            cost[i][0] = cost[i-1][0] + grid[i][0]

        for i in range(1,col):
            cost[0][i] = cost[0][i-1] + grid[0][i]

        for i in range(1,row):
            for j in range(1,col):
                if cost[i][j-1] > cost[i-1][j]:
                    cost[i][j] = cost[i-1][j] + grid[i][j]
                else:
                    cost[i][j] = cost[i][j-1] + grid[i][j]

        return cost[row-1][col-1]

def printM(a):
    row = len(a)
    col = len(a[0])
    for i in range(row):
        for j in range (col):
            print (a[i][j], end=' ')
        print()
    print('-----------------')

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
            
            ret = Solution().minPathSum(grid)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()

