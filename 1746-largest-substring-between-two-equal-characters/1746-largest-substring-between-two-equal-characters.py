class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_string = {}
        indices = {}
        max_len = -1
        for i, char in enumerate(s):
            if char not in indices:
                indices[char] = [i]
            else:
                indices[char].append(i)
        
        for char, positions in indices.items():
            max_len = max(max_len, positions[-1] - positions[0] - 1)
        
        return max_len