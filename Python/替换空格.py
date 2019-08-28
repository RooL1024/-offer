# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        p1 = len(s) - 1
        res = list(s)
        n = s.count(' ')
        res += [0]*n*2
        p2 = len(res) - 1
        while p1 != p2:
            if res[p1] == ' ':
                res[p2] = '0'
                res[p2-1] = '2'
                res[p2-2] = '%'
                p2 -= 3
            else:
                res[p2] = res[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(res)