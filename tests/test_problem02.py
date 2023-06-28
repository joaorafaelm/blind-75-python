from problems.problem02 import solution


def test():
    assert solution('abcabcbb') == 3
    assert solution('bbbbb') == 1
    assert solution('pwwkew') == 3
