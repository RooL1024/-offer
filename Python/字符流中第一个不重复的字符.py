# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.string_all = {}
        self.ch = []
    def FirstAppearingOnce(self):
        # write code here
        if self.string_all is None:
            return '#'
        for i in self.ch:
            if self.string_all[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.ch.append(char)
        if char in self.string_all:
            self.string_all[char] = self.string_all[char] + 1
        else:
            self.string_all[char] = 1