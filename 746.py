# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:54:36 2018

@author: NickYue
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2]+cost[i],dp[i-1]+cost[i])
        return min(dp[len(cost)-1],dp[len(cost)-2])

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
            cost = stringToIntegerList(line)
            
            ret = Solution().minCostClimbingStairs(cost)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()