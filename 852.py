# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:10:27 2018

@author: NickYue
"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """        
        left = 1
        right = len(A) - 2
        while left < right:
            mid = (right + left) // 2
            if A[mid] < A[mid+1]:
                left = mid + 1
            if A[mid] > A[mid+1]:                
                right = mid
        return left

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
            A = stringToIntegerList(line)
            
            ret = Solution().peakIndexInMountainArray(A)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()