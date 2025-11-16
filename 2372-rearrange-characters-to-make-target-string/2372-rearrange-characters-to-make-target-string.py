class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # s = Counter(s)
        # target = Counter(target)
        # counter = 0
        # while True:
        #     for char, count in target.items():
        #         if char not in s or s[char] < count:
        #             return counter
        #         s[char] -= count
        #     counter += 1
        # return counter
        s_count = Counter(s)
        t_count = Counter(target)

        # For each char in target, compute how many times it can be formed
        # using s, then return the minimum of those.
        return min(s_count[c] // t_count[c] for c in t_count)