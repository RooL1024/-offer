# -*- coding:utf-8 -*-
import math
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 分析出递归条件：    我们用f(n)来表示跳n级台阶的跳法数量，
        #                    f(1) = 1
        # 表示跳1级台阶的跳法数量;
        #
        #                    f(2) = 2
        # 表示跳2级台阶的跳法数量;
        #
        #                    f(3) = f(2) + f(1) + 1  我们可以递推出  f(n) = f(n - 1) + f(n - 2) + ** *+f(1) + 1,
        #
        #                  而f(n - 1) = f(n - 2) + ** *+f(1) + 1。
        #
        #                 将两式相减可以求出递推公式，也即是
        # f(n) - f(n - 1) = f(n - 1)，即f(n) = 2 * f(n - 1);
        # 所以自底向上的动态规划方法浮出眼前。
        if number == 0 or number == 1:
            return number
        else:
            return math.pow(2,number-1)

