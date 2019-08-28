# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array == None or len(array) <= 0:
            return 0

        opt = [0] * len(array)
        opt[0] = array[0]
        for i in range(1, len(array)):
            if opt[i - 1] <= 0:
                opt[i] = array[i]
            else:
                opt[i] = array[i] + opt[i - 1]

        return max(opt)