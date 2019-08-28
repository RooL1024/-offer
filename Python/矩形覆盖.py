# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        # 斐波那契数列
        if number <= 0:
            return 0
        list = [1, 2]
        while number >= 2:
            list[0], list[1] = list[1], list[0] + list[1]
            number -= 1
        return list[0]

