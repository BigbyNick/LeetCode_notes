# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 16:20:11 2018

@author: NickYue
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) ==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[len(nums)-1]

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
            
            ret = Solution().rob(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break
if __name__ == '__main__':
    main()