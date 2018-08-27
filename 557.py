# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:57:32 2018

@author: NickYue
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        lists = s.split(' ')
        
        for i in range(len(lists)):
            res = res + lists[i][::-1]
            if i != len(lists)-1:
                res = res+' '
        return res

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
            s = stringToString(line)
            
            ret = Solution().reverseWords(s)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()