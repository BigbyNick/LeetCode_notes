# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 16:44:33 2018

@author: NickYue
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        dp = [0] 
        while len(dp) <= num :
            dp_2 = []
            for ele in dp:
                dp_2.append(ele + 1)
            dp = dp + dp_2
            
        return dp[:num+1]

def stringToInt(input):
    return int(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            num = stringToInt(line)
            
            ret = Solution().countBits(num)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()