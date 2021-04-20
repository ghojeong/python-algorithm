# https://leetcode.com/problems/reverse-string/

from .sol2_1 import Solution as Solution1
from .sol2_2 import Solution as Solution2

def test(solution, s: str) -> bool:
    expected = s[::-1]
    actualList = list(s)
    solution.reverseString(actualList)
    actual = "".join(actualList)
    return actual == expected

def printTest(solution, tag: str):
    tested = test(solution, "hello") and test(solution, "olleh")
    result = "Pass: " if tested is True else "Fail: "
    print(result + tag)

def test_1():
    printTest(Solution1(), "2_1")
    printTest(Solution2(), "2_2")
    print()

test_1()
