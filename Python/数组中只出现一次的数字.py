# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array) == 1:
            return []

        res = [0,0]
        temp = 0
        index = 0
        for i in array:
            temp ^= i
        while temp & 1 == 0 and index <32:
            temp = temp >> 1
            index += 1
        for e in array:
            if (e>>index)&1 == 1:
                res[0] = res[0]^e
            else:
                res[1] = res[1]^e
        return res