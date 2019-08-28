# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if self.getDepth(pRoot) == -1:
            return False
        return True
    def getDepth(self,root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        if left == -1:
            return -1
        right = self.getDepth(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left,right) + 1