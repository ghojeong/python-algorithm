# https://leetcode.com/problems/group-anagrams/

from typing import List
from sol5_1 import Solution as Solution1

def test(solution, input: List[str], expected: List) -> bool:
    actual = solution.groupAnagrams(input)
    sortedActual = sorted(map(sorted, actual))
    sortedExpected = sorted(map(sorted, expected))
    return sortedActual == sortedExpected

def printTest(solution, tag: str):
    input1 = ["eat","tea","tan","ate","nat","bat"]
    expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]

    tested1 = test(solution, input1, expected1)

    result1 = "Pass Example1: " if tested1 is True else "Fail: "
    print(result1 + tag)

def test_1():
    printTest(Solution1(), "5_1")
    print()

test_1()
