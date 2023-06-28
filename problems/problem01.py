'''
Blind Curated 75 - Problem 01
=============================

Two Sum
-------

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/two-sum/
'''

def solution(nums, target):
    complements = set()
    for i, num in enumerate(nums):
        if (complement := target - num) in complements:
            return [nums.index(complement), i]
        complements.add(num)
