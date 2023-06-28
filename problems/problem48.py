'''
Blind Curated 75 - Problem 48
=============================

Word Search 2
-------------

Given a grid of characters and a set of words, find all the words from the set
that can be found in the grid.

Words can be constructed from letters in sequentially adjacent cells, where
adjacent cells are ones neighboring either horizontally or vertically. The same
letter may not be used more than once in a word.

Assume all characters are lower case English letters.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/word-search-ii/
'''


from collections import defaultdict


class TrieNode:
	def __init__(self):
		self.children = defaultdict(TrieNode)
		self.word = ''
	def insert(self, word, i=0):
		if i == len(word):
			self.word = word
		else:
			self.children[word[i]].insert(word, i + 1)


def solution(board, words):
    pass
