# -*- coding=utf-8 -*-
#@author: vincentping@gmail.com
#@github: https://github.com/vincentping
#@date: 2014-12-10

"""
https://oj.leetcode.com/problems/add-binary/

Problem: 
Add Binary

Description: 
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Tags: Math, String

Difficulty: Easy

The Python model is:
---------------------------------
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
----------------------------------
"""

def addBinary(a, b):
    return bin(int(a,2)+int(b,2))[2:]

if __name__ == '__main__':
    a = '10'
    b = '111'
    
    print addBinary(a,b)
#EOF