'''
Blind Curated 75 - Problem 35
=============================

Word Break
----------

Given a non-empty string and a list of non-empty words, find whether the string
can be segmented into a sequence of one or more words.

Note that the same word may be used multiple times. Assume there are no
duplicate words.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/word-break/
'''

import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = ''

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.word = word


class Solution:
    def word_break(self, s, words):
        pass

    def _search_from(self, i):
        pass
