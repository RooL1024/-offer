# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minNum = float('inf')

    def push(self, node):
        # write code here
        if node < self.minNum:
            self.minNum = node
            self.minStack.append(self.minNum)
        self.stack.append(node)

    def pop(self):
        # write code here
        if self.stack != []:
            if self.stack[-1] == self.minNum:
                self.minStack.pop()
            self.stack.pop(-1)

    def top(self):
        # write code here
        if self.stack != []:
            return self.stack[-1]
        else:
            return None


    def min(self):
        # write code here

        return self.minStack[-1]