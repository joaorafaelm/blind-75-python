'''
Blind Curated 75 - Problem 09
=============================

Merge k Sorted Lists
--------------------

Merge _k_ sorted linked lists and return it as one sorted list.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/merge-k-sorted-lists/
'''

import heapq


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __eq__(self, o):
		return self.val == o.val

	def __lt__(self, o):
		return self.val < o.val

	def __le__(self, o):
		return self.val <= o.val


def solution(lists):
    pass
