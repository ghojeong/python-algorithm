from sol1_1 import Solution as Solution1

def test(solution) -> bool:
    trueExpected = solution.isPalindrome("A man, a plan, a canal: Panama")
    falseExpected = solution.isPalindrome("race a car")
    # print(trueExpected)
    # print(falseExpected)
    return trueExpected and not falseExpected

def printTest(solution, tag: str):
    result = "Pass: " if test(solution) is True else "Fail: "
    print(result + tag)

printTest(Solution1(), "1_1")
