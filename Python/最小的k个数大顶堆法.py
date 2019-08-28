# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        max_heap = []
        length = len(tinput)
        if not tinput or k <= 0 or k > length:
            return []
        k = k - 1
        for element in tinput:
            element = -element
            if len(max_heap) <= k:
                heapq.heappush(max_heap,element)
            else:
                heapq.heappushpop(max_heap,element)
        return sorted(map(lambda x:-x,max_heap))