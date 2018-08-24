# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:33:18 2018

@author: NickYue
"""
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        lists = []
        for ele in words:
            word = ""
            for char in ele:
                word = word + code[ord(char)-97]
            if word not in lists:
                lists.append(word)
        return len(lists)

def stringToStringArray(input):
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
            words = stringToStringArray(line)
            
            ret = Solution().uniqueMorseRepresentations(words)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()