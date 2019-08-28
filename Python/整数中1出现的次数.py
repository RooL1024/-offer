# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        s = str(n)
        length = len(s)
        for idx, i in enumerate(s):
            place = length - idx  # 当前位数（个位是1，十位是2……）
            pre = n // (10 ** place)  # 当前位数的高位数字
            aft = n % (10 ** (place - 1))  # 当前位数的低位数字
            if i == '0':
                res += pre * 10 ** (place - 1)
            elif i == '1':
                res += pre * 10 ** (place - 1) + aft + 1
            else:
                res += (pre + 1) * 10 ** (place - 1)
        return res
