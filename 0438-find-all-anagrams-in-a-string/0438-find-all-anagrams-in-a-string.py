class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        p = Counter(p)
        indices = []
        for i in range(n - k + 1):
            part = Counter(s[i:i+k])
            for char, count in part.items():
                if p[char] != count:
                    break
            else:
                indices.append(i)
        return indices
