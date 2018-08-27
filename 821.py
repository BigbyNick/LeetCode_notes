# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:58:19 2018

@author: NickYue
"""

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(S)):
            left , right = S[i-len(S)::-1].find(C) , S[i:].find(C)
            if left == -1: left = 10000
            if right == -1: right = 10000
            res.append(min(left , right)) 
        return res

def stringToString(input):
    return input[1:-1].decode('string_escape')

def stringToChar(line):
    if not line:
        return ''
    c = line[0]
    if len(line) == 1:
        line = '"%s"' % c
    elif len(line) == 2 and c == '\\':
        c = line[1]
        line = '"\\%s"' % c
    return json.loads(line)

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
            S = stringToString(line)
            line = lines.next()
            C = stringToChar(line)
            
            ret = Solution().shortestToChar(S, C)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()