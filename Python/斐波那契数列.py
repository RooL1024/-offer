# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        fibonacci0 = 0
        fibonacci1 = 1
        fibonaccin = 0
        if n == 0 or n == 1:
            return n
        for i in range(2,n+1):
            fibonaccin = fibonacci0 + fibonacci1
            fibonacci0 = fibonacci1
            fibonacci1 = fibonaccin
        return fibonaccin


