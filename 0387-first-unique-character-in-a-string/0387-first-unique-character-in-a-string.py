class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s) # Stores frequencies of chars
 
        for i, char in enumerate(s):
            if s_count[char] == 1: # The first char with count 1 should be returned
                return i
        return -1