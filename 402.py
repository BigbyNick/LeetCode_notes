# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:48:49 2018

@author: NickYue
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        if k >= len(num):
            return "0"
        i = 0
        while i < len(num) - 1 and k > 0:#开始搜索
            if(int(num[i])>int(num[i+1])):#如果有一位数字大于下一位，那么将这一位删除
                num = num[0:i]+num[i+1:]
                if i > 0:
                    i -= 1
                k -= 1
            else:
                i += 1
        num = num[:len(num)-k]
        return str(int(num))

def stringToString(input):
    return input[1:-1].decode('string_escape')

def stringToInt(input):
    return int(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            num = stringToString(line)
            line = lines.next()
            k = stringToInt(line)
            
            ret = Solution().removeKdigits(num, k)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()