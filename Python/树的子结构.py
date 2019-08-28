# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None or pRoot1 == None:
            return False
        return self.isSubtree(pRoot1,pRoot2)

    def isSubtree(self,tree1,tree2):
        if tree2 == None:
            return True
        if tree1 == None:
            return tree1 == tree2

        res = False

        if tree1.val == tree2.val:
            res = self.isSubtree(tree1.left,tree2.left) and self.isSubtree(tree1.right,tree2.right)
        return res or self.isSubtree(tree1.left,tree2) or self.isSubtree(tree1.right,tree2)