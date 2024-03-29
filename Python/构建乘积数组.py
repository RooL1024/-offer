class Solution:
    def multiply(self, A):
        # write code here
        if not A or len(A) < 0:
            return 0
        length = len(A)
        B = [1] * length
        # 下三角，从1开始乘的
        for i in range(1, length):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        # 上三角，接着下三角从大往小乘，节约空间，最后一位设为1，前面只有一位，在于之前计算好的相乘
        # 画一个矩形就明白了。
        for i in range(length - 2, -1, -1):
            temp = temp * A[i + 1]
            B[i] *= temp
        return B