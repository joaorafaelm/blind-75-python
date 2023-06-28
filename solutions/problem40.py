'''
Blind Curated 75 - Problem 40
=============================

Reverse Bits
------------

Reverse the bits of a given 32-bit unsigned integer.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/reverse-bits/
'''


def solution(n):
    '''
    Working inwards from both ends, use bitwise logic to swap each pair of bits.
    '''
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))

    return res
