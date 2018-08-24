# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:48:25 2018

@author: NickYue
"""

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        #area为dict，键为域名，值为次数
        area = {}
        #对于每一个网站
        for ele in cpdomains:
            #分离次数和网址，times为次数，key为网址
            times = int(ele.split(' ')[0])
            key = ele.split(' ')[1]
            #keys 是域名集合，判断当前域名是否存在，不存在新建，存在则+=times
            keys = key.split('.')
            https = ''
            for i in keys[::-1]:
                if https == '':
                    https = i
                else:
                    https = i + '.' + https
                if https not in area.keys():
                    area[https] = times
                else:
                    area[https] += times
            #得到area
        
        res = []
        for key,values in area.items():
            res.append(str(str(values)+' '+key))
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
            cpdomains = stringToStringArray(line)
            
            ret = Solution().subdomainVisits(cpdomains)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()