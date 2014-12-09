# -*- coding=utf-8 -*-
#@author: vincentping@gmail.com
#@github: https://github.com/vincentping
#@date: 2014-12-9

"""
https://oj.leetcode.com/problems/min-stack/

Problem: 
Min Stack

Description: 
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Tags: Stack, Data Structure

Difficulty: Easy

The Python model is:
---------------------------------
class MinStack:
    # @param x, an integer
    # @return an integer
    def push(self, x):
        

    # @return nothing
    def pop(self):
        

    # @return an integer
    def top(self):
        

    # @return an integer
    def getMin(self):
----------------------------------
"""
class MinStack:
    def __init__(self):
        self.L = []
        self.minL = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.L) == 0:
            self.minL.append(x)
        else:
            if x <= self.minL[-1]:
                self.minL.append(x)
        self.L.append(x)

    # @return nothing
    def pop(self):
        if len(self.L)>0 and self.L.pop() == self.minL[-1]:
            self.minL.pop()

    # @return an integer
    def top(self):
        return self.L[-1]

    # @return an integer
    def getMin(self):
        return self.minL[-1]

#EOF