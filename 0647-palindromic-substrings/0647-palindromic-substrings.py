class Solution:
    def expand(self, s, left, right):
        counter = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            counter += 1
            left -= 1
            right += 1
        return counter

        
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            even = self.expand(s, i, i + 1)
            odd = self.expand(s, i, i)
            counter += even
            counter += odd
        return counter