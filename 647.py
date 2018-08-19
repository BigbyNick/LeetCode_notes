# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:36:59 2018

@author: NickYue
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += 1
            left = i-1
            right = i +1
            while left >=0 and right<len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            left = i
            right = i+1
            while left >=0 and right<len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            s = stringToString(line)
            
            ret = Solution().countSubstrings(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()