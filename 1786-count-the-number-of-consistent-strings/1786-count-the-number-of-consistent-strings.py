class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0

        allowed = set(allowed)

        for word in words:
            for char in word:
                if char not in allowed:
                    counter += 1
                    break
        return len(words) - counter