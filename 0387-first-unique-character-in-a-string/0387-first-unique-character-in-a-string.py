class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)

        for char, count in s_count.items():
            if count == 1:
                return s.index(char)
        return -1