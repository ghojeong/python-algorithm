

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char)
        return "".join(strs[:]) == "".join(strs[::-1])
