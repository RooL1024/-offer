# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or n <= 0:
            return s

        s = list(s)
        self.reverse(s,0,n-1)
        self.reverse(s,n,len(s)-1)
        self.reverse(s,0,len(s)-1)
        return ''.join(s)




    def reverse(self,s,start,end):
        while start < end:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
