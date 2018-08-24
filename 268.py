# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:43:15 2018

@author: NickYue
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method one 从数学角度考虑
        return int(len(nums)*(len(nums)+1)/2 - sum(nums))

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
            nums = stringToIntegerList(line)
            
            ret = Solution().missingNumber(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()