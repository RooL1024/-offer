# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        res = None
        while pHead!= None:
            temp = pHead.next
            pHead.next = res
            res = pHead
            pHead = temp

        return res
