# -*- coding=utf-8 -*-
#@author: vincentping@gmail.com
#@github: https://github.com/vincentping
#@date: 2014-12-9

"""
https://oj.leetcode.com/problems/reverse-words-in-a-string/

Problem: 
Reverse Words in a String

Description: 
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification:
* What constitutes a word?
    A sequence of non-space characters constitutes a word.
* Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.
* How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.

Tags: String

Difficulty: Medium

The Python model is:
---------------------------------
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
----------------------------------
"""

def reverseWords(s):
    li = s.split()
    return ' '.join(reversed(li))

if __name__ == '__main__':
    ss = ("the sky is blue",
             "  Hello   darkness my old     friend     ",
            )
    for s in ss:
        print 'Origin: ', s
        print 'Reversed:', reverseWords(s)
        print ' '*50
#EOF