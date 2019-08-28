# -*- coding:utf-8 -*-
class Solution:

    def NumberOf1(self, n):
        # write code here
        INT_BITS = 32
        MAX_INT = (1 << (INT_BITS - 1)) - 1
        count = 0
        while n:
            if n < - MAX_INT - 1 or n > MAX_INT:
                break
            count += 1
            n = (n-1)&n
        return count
