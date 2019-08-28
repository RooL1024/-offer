# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) <= 1:
            return array

        left = 0
        right = len(array) - 1

        while left < right:
            while left < right and array[left] & 1 == 1:
                left += 1
            while left < right and array[right] & 1 == 0:
                right -= 1
            if left < right:
                temp = array[right]
                array[right] = array[left]
                array[left] = temp
        return array

