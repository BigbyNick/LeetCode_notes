# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:49:16 2018

@author: NickYue
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        set_candies = set(candies)
        
        if len(set_candies) >= len(candies)//2:
            return len(candies)//2
        else:
            return len(set_candies)

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
            candies = stringToIntegerList(line)
            
            ret = Solution().distributeCandies(candies)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()