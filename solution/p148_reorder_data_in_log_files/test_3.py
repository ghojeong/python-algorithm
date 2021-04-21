# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List
from sol3_1 import Solution as Solution1

def test(solution, input: List[str], expected: List[str]) -> bool:
    actual = solution.reorderLogFiles(input)
    return bool(set(actual).intersection(expected))

def printTest(solution, tag: str):
    input1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    expected1 = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

    input2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    expected2 = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

    tested1 = test(solution, input1, expected1)
    tested2 = test(solution, input2, expected2)

    result1 = "Pass Example1: " if tested1 is True else "Fail: "
    print(result1 + tag)

    result2 = "Pass Example2: " if tested2 is True else "Fail: "
    print(result2 + tag)

def test_1():
    printTest(Solution1(), "3_1")
    print()

test_1()
