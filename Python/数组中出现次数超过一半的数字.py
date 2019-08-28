# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 这个操作就是建立在出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，所以如果存在这个数，最后count
        # 肯定不为0的
        count = 1
        number = numbers[0]
        for i in numbers[1:]:
            if number == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    number = i
                    count += 1

        sum = 0
        for j in numbers:
            if j == number:
                sum += 1

        return number if sum > len(numbers) // 2 else 0



