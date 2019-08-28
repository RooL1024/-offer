# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        max_sum = array[0]
        pre_sum = 0
        for i in array:
            if pre_sum < 0:
                pre_sum = i
            else:
                pre_sum += i
            if pre_sum > max_sum:
                max_sum = pre_sum
        return max_sum

