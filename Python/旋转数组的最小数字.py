# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        front,rear = 0,len(rotateArray)-1
        midIndex = 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                break
            midIndex = (front + rear) // 2
            if rotateArray[front] == rotateArray[rear] and rotateArray[front] == rotateArray[midIndex]:
                return self.shunxuchahzao(rotateArray,front,rear)
            if rotateArray[front] <= rotateArray[midIndex]:
                front = midIndex
            elif rotateArray[rear] >= rotateArray[midIndex]:
                rear = midIndex
        return rotateArray[midIndex]



    def shunxuchahzao(self,array,start,end):
        res = array[0]
        for i in array[start:end+1]:
            if i < res:
                res = i
        return res