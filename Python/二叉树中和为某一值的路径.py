# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        if not root:
            return res
        path = [root.val]
        self.target = expectNumber
        self.dfs(root,res,path)
        return res

    def dfs(self,root,res,path):
        if not root.left and not root.right and sum(path) == self.target:
            res.append(path)
        if root.left:
            self.dfs(root.left,res,path + [root.left.val])
        if root.right:
            self.dfs(root.right,res,path + [root.right.val])