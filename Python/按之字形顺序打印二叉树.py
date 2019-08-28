# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        stack1 = [pRoot]
        stack2 = []
        result = []
        while (stack1 or stack2):
            ret1 = []   # 用来暂时存储各层节点的值
            ret2 = []   # 用来暂时存储各层节点的值
            while stack1:
                node = stack1.pop()
                # 先左后右入栈2
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
                ret1.append(node.val)
            if len(ret1) != 0:
                result.append(ret1)
            while stack2:
                node = stack2.pop()
                # 先右后左入栈1
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
                ret2.append(node.val)
            if len(ret2) != 0:
                result.append(ret2)
        return result
