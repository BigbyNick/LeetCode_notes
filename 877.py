# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:44:25 2018

@author: NickYue
"""
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if len(piles) == 2:
            return True
        p_len = len(piles)
        dp = [([0] * p_len) for i in range(p_len)]
        for i in range(p_len):
            dp[i][i] = piles[i]

        for i in range(0,p_len):
            for j in range(1,p_len - i):
                dp[i][i+j] = max(piles[i+j]-dp[i][i+j-1], piles[i]-dp[i+1][i+j])
        return (dp[0][len(piles)-1] > 0)

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
            piles = stringToIntegerList(line)
            
            ret = Solution().stoneGame(piles)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()