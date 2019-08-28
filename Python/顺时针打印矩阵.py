# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        res = []
        row = len(matrix)
        col = len(matrix[0])
        circle = (min(row, col) - 1) // 2 + 1
        left, top, right, buttom = 0, 0, col - 1, row - 1
        for i in range(circle):
            for j in range(left, right + 1):
                res.append(matrix[i][j])
            for j in range(top + 1, buttom + 1):
                res.append(matrix[j][right])
            if top != buttom:
                for j in range(right - 1, left - 1, -1):
                    res.append(matrix[buttom][j])
            if left != right:
                for j in range(buttom - 1, top, -1):
                    res.append(matrix[j][left])
            left += 1
            right -= 1
            top += 1
            buttom -= 1
        return res