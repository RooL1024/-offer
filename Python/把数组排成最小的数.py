# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        str_num = [str(num) for num in numbers]
        flag = True
        count = len(str_num) - 1
        while flag and count > 0:
            flag  = False
            for i in range(len(str_num)-1):
                if self.max_str(str_num[i],str_num[i+1]) == str_num[i]:
                    temp = str_num[i]
                    del str_num[i]
                    str_num.insert(i+1,temp)
                    flag = True
            count -= 1
        string = ''.join(str_num)
        return string



    def max_str(self,str1,str2):

        return str1 if str1+str2 > str2+str1 else str2
