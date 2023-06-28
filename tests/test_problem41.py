import unittest
from problems.problem40 import solution


class Test(unittest.TestCase):
    def test(self):
        bits = '00000010100101000001111010011100'
        self.assertEqual(solution(int(bits, 2)), 964176192)
        bits = '11111111111111111111111111111101'
        self.assertEqual(solution(int(bits, 2)), 3221225471)
