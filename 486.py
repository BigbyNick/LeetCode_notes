# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:10:39 2018

@author: NickYue
"""

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        p_len = len(nums)
        dp = [([0] * p_len) for i in range(p_len)]
        for i in range(p_len):
            dp[i][i] = nums[i]

        for i in range(p_len-2, -1, -1):
            for j in range(i, p_len):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return (dp[0][p_len-1] >= 0)

def stringToIntegerList(input):
    return json.loads(input)

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
            
            ret = Solution().PredictTheWinner(nums)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()