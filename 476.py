# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:10:56 2018

@author: NickYue
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        #从第一位开始一位一位按位异或获得补数
        while num >= i:
            # ^表示按位进行亦或运算
            num ^= i
            # 各二进位全部左移若干位,高位丢弃,低位补0
            i <<= 1
        return num

def stringToInt(input):
    return int(input)

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
            num = stringToInt(line)
            
            ret = Solution().findComplement(num)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()