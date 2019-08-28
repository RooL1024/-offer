# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode

        if pNode.right:
            node_next = pNode.right
            while node_next.left:
                node_next = node_next.left
            return node_next

        while pNode.next:
            temp = pNode.next
            if temp.left == pNode:
                return temp
            pNode = temp

