# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        first = ListNode(-1)
        first.next = pHead
        last = first
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                value = pHead.val
                while pHead and pHead.val == value:
                    pHead = pHead.next
                last.next = pHead
            else:
                last = pHead
                pHead = pHead.next
        return first.next