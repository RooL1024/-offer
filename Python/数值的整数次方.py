# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent < 1:
            return 1 / self.getPower(base, -exponent)
        else:
            return self.getPower(base, exponent)


    def getPower(self,base,exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        res = self.Power(base,exponent>>1)
        res *= res
        if exponent & 1 == 1:
            res *= base
        return res

