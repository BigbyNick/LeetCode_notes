# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:48:05 2018

@author: NickYue
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyset=['qwertyuiop','asdfghjkl','zxcvbnm']
        res = []
        for ele in words:
            ele_l = set(ele.lower())
            for key in keyset:
                if ele_l.issubset(set(key)):
                    res.append(ele)
        return res

def stringToStringArray(input):
    return json.loads(input)

def stringArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            words = stringToStringArray(line)
            
            ret = Solution().findWords(words)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()