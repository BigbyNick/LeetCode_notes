# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:30:42 2018

@author: NickYue
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        for i in range(len(haystack)-l+1):
            if haystack[i:i+l] == needle:
                return i
        return -1

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
            haystack = stringToString(line)
            line = lines.next()
            needle = stringToString(line)
            
            ret = Solution().strStr(haystack, needle)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()