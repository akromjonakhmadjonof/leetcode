class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s = Counter(s)
        target = Counter(target)
        counter = 0
        while True:
            for char, count in target.items():
                if char not in s or s[char] < count:
                    return counter
                s[char] -= count
            counter += 1
        return counter