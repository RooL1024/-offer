# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []

        res = []
        small = 1
        big = 2
        curSum = 0
        while small < big:
            curSum = sum(range(small,big+1))
            if curSum == tsum:
                res.append(range(small,big+1))
                big += 1
            elif curSum < tsum:
                big += 1
            else:
                small += 1
        return res
