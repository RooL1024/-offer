# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        num = 0
        if data:
            first = self.getFirstK(data, k , 0, len(data) - 1)
            last = self.getLastK(data, k, 0, len(data) - 1)
            if first > -1 and last > -1:
                num = last - first + 1
        return num

    def getFirstK(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        midD = data[mid]
        if midD > k:
            end = mid - 1
        elif midD < k:
            start = mid + 1
        else:
            if (mid == 0) or (mid > 0 and data[mid - 1] != k):
                return mid
            else:
                end = mid - 1
        return self.getFirstK(data, k, start, end)

    def getLastK(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        midD = data[mid]
        if midD > k:
            end = mid - 1
        elif midD < k:
            start = mid + 1
        else:
            if (mid == len(data) - 1) or (mid < len(data) - 1 and data[mid + 1] != k):
                return mid
            else:
                start = mid + 1
        return self.getLastK(data, k, start, end)