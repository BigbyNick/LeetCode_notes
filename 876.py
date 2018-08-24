# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:12:12 2018

@author: NickYue
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def listlen(self, node):
        len_l = 1
        while node.next:
            len_l += 1
            node = node.next
        return len_l
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        len_l = self.listlen(head)
        n = len_l // 2
        node = head
        for i in range(n):
            node = node.next
        return node

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            head = stringToListNode(line)
            
            ret = Solution().middleNode(head)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()