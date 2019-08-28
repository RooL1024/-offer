# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        index = 0
        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                index = i
                break
        for j in range(index,len(sequence)):
            if sequence[j] < sequence[-1]:
                return False
        left = True
        right = True
        if len(sequence[:index]) > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        if len(sequence[index:-1]) > 0:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return left and right