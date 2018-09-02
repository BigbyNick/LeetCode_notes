# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 22:02:17 2018

@author: NickYue
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        profit = 0
        for i in range(days-1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])
                
        return profit

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
            prices = stringToIntegerList(line)
            
            ret = Solution().maxProfit(prices)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()