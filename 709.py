# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:09:47 2018

@author: NickYue
"""

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            str = stringToString(line)
            
            ret = Solution().toLowerCase(str)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()