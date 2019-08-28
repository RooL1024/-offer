# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        dummy = pHead

        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext

        dummy = pHead

        while dummy:
            dummyrandom = dummy.random
            copynode = dummy.next
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy = copynode.next

        dummy = pHead
        copyhead = pHead.next
        while dummy:
            copynode = dummy.next
            dummynext = copynode.next
            dummy.next = dummynext
            if dummynext:
                copynode.next = dummynext.next
            else:
                copynode.next = None
            dummy = dummynext
        return copyhead




