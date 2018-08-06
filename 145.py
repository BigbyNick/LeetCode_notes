# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:32:03 2018

@author: NickYue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#后序遍历有一种巧妙的方式：前序遍历根节点，先后将左右子节点压栈。
#这样的遍历顺序为：中，右，左。最后reverse结果，则遍历结果变为：左，右，中。

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        res = []
        if root == None:
            return []
        queue.append(root)
        while (queue):
            cur_node = queue.pop()
            res.append(cur_node.val)            
            if cur_node.left :
                queue.append(cur_node.left)
            if cur_node.right :
                queue.append(cur_node.right)
        return res[::-1]
