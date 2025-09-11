class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s) # Stores frequencies of chars
 
        for char, count in s_count.items():
            if count == 1: # The first char with count 1 should be returned
                return s.index(char)
        return -1