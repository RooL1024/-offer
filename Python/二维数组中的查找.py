# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        cols = len(array[0]) - 1
        row = 0
        if len(array) == 0 or len(array[0]) == 0 or array[0][0] > target or array[rows-1][cols] < target:
            return False
        while row < rows and cols >= 0:
            if array[row][cols] > target:
                cols -= 1
            elif array[row][cols] < target:
                row += 1
            else:
                return True
        return False





