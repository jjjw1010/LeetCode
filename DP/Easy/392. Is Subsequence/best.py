class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if char in t:
                t = t.split(char, 1)[1]
            else:
                return False
        return True
