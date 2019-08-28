# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        # 第一次跳一级的时候跳法数目等于后面n-1级台阶的跳法数目，同理，第一次跳2级的时候
        # 跳法数目等于后面n-2级台阶的跳法数目，所以本题目是斐波那契数列
