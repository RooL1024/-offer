# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0

        p_left = self.TreeDepth(pRoot.left)
        p_right = self.TreeDepth(pRoot.right)

        return max(p_left,p_right) + 1