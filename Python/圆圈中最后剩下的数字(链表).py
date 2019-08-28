# -*- coding:utf-8 -*-

class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None



class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1:
            return -1

        node = self.create_cycle(n)
        prev = None
        start = 1
        index = start
        while node and node.next:
            if index == m:
                if prev.next != prev:
                    prev.next = node.next
                    node.next = None
                    node = prev.next
                    index = start
                else:
                    return prev.value
            else:
                prev = node
                node = node.next
                index += 1

        # 创建循环单链表，值从1开始
    def create_cycle(self,n):
        head = LinkNode(0)
        prev = head
        index = 1
        while n - 1 > 0:
            curr = LinkNode(index)
            prev.next = curr
            prev = curr
            index += 1
            n -= 1
        curr.next = head
        return head