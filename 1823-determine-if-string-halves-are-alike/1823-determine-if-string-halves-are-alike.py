from collections import Counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        first, second = Counter(s[:n]), Counter(s[n:])
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        total = 0
        for char, count in first.items():
            if char in vowels:
                total += count
        for char, count in second.items():
            if char in vowels:
                total -= count
        return total == 0