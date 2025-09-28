class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced = 0
        counter = 0
        for char in s:
            balanced += 1 if char == "L" else -1
            if balanced == 0:
                counter += 1
        return counter