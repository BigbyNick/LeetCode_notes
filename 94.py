# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

List_in = []
class Solution(object):
    def get_in(self, node = None):
        global List_in
        if node :
            self.get_in(node.left)
            List_in.append(node.val)
            self.get_in(node.right)
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global List_in
        List_in = []
        if root == None:
            return []
        else:
            self.get_in(root)

        return List_in