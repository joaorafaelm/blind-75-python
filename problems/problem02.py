'''
Blind Curated 75 - Problem 02
=============================

Longest Substring Without Repeating Characters
----------------------------------------------

Given a string, find the length of the longest substring without repeating
characters.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


def solution(string):
    max_length = length = 0
    letters = ''

    for letter in string:
        length = 1 if letter in letters else length + 1
        letters += letter
        max_length = max(max_length, length)

    return max_length
