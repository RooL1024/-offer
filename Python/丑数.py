# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        baselist = [1]
        min2 = min3 = min5 = 0
        count = 1
        while count < index:
            minnum = min(baselist[min2]*2,baselist[min3]*3,baselist[min5]*5)
            baselist.append(minnum)
            while baselist[min2] * 2 <= minnum:
                min2 += 1
            while baselist[min3] * 3 <= minnum:
                min3 += 1
            while baselist[min5] * 5 <= minnum:
                min5 += 1
            count += 1
        return baselist[-1]