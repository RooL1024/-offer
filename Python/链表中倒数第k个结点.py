# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or not k:
            return None

        pfast = head
        pslow = head

        for i in range(k-1):
            if not pfast.next:
                return None
            pfast = pfast.next
        while pfast.next:
            pslow = pslow.next
            pfast = pfast.next
        return pslow

