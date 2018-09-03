# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:13:45 2018

@author: NickYue
"""

from collections import defaultdict
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        res = []
        direct="Y+"
        x,y=0,0
        d={("Y+",-1):"X+",("Y+",-2):"X-",("Y-",-1):"X-",("Y-",-2):"X+",("X+",-1):"Y-",("X+",-2):"Y+",("X-",-1):"Y+",("X-",-2):"Y-"}
        d1=defaultdict(int)
        for i in obstacles:
            d1[(i[0],i[1])]=1
        for i in commands:
            if i==-1:
                direct=d[(direct,i)]
            elif i==-2:
                direct=d[(direct,i)]
            else:
                if direct=="X+":
                    for j in range(i):
                        x+=1
                        if d1[(x,y)]==1:
                            x-=1
                            break
                elif direct=="X-":
                    for j in range(i):
                        x-=1
                        if d1[(x,y)]==1:
                            x+=1
                            break
                elif direct=="Y+":
                    for j in range(i):
                        y+=1
                        if d1[(x,y)]==1:
                            y-=1
                            break
                else:
                    for j in range(i):
                        y-=1
                        if d1[(x,y)]==1:
                            y+=1
                            break
                res.append(pow(x,2)+pow(y,2))
        return max(res)

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt2dArray(input):
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
            commands = stringToIntegerList(line)
            line = lines.next()
            obstacles = stringToInt2dArray(line)
            
            ret = Solution().robotSim(commands, obstacles)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()