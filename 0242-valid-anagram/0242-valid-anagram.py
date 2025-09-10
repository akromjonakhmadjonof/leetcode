class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        for char, count in s_count.items():
            if t_count[char] != count:
                return False
        return True