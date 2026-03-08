class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = second = 0

        while second < len(t) and first < len(s):
            if t[second] == s[first]:
                first += 1
            second += 1
        return first == len(s)