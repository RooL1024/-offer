# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pHead1_lenth = 0
        pHead2_lenth = 0

        p1 = pHead1
        p2 = pHead2
        while p1:
            pHead1_lenth += 1
            p1 = p1.next
        while p2:
            pHead2_lenth += 1
            p2 = p2.next
        if pHead2_lenth > pHead1_lenth:
            pHead1, pHead2 = pHead2, pHead1
        dis = abs(pHead2_lenth - pHead1_lenth)

        while dis > 0:
            pHead1 = pHead1.next
            dis -= 1
        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1




