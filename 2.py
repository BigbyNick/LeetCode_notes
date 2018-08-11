# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 22:59:15 2018

@author: NickYue
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def jinwei(self, head):
        node = head
        while node :
            if node.val > 9:
                node.val = node.val - 10
                if node.next :
                    node.next.val += 1
                else:
                    node.next = ListNode(1)
            node = node.next
            
        return head
        
    def addOperation(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            l1.val = l1.val + l2.val
            l1.next = self.addOperation(l1.next, l2.next)
            return l1        
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = self.addOperation(l1, l2)
        res = self.jinwei(res)
        return res
