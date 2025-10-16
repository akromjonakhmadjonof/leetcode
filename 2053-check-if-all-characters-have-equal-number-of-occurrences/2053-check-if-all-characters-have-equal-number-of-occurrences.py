class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = Counter(s)
        target = None
        for char, count in s.items():
            if not target:
                target = count
            elif target != count:
                return False
        return True