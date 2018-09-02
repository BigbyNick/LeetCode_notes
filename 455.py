# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 22:04:25 2018

@author: NickYue
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        n_child = len(g)
        n_cookies = len(s)
        index = 0
        tol = 0
        childs = sorted(g)
        cookies = sorted(s)
        for i in range(n_cookies):
            if cookies[i] >= childs[index]:
                tol += 1
                index += 1
            if index >= n_child:
                break
        return tol

def stringToIntegerList(input):
    return json.loads(input)

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
            g = stringToIntegerList(line)
            line = lines.next()
            s = stringToIntegerList(line)
            
            ret = Solution().findContentChildren(g, s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()