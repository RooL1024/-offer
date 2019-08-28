# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []

        left = 0
        right = len(array) - 1
        res = []

        while left < right:
            if array[left] + array[right] < tsum:
                left += 1
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                res.append(array[left])
                res.append(array[right])
                break
        return res