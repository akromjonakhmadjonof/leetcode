from collections import Counter
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights) # Sort heights as expected
        total = 0 # Stores differences count
        for i, num in enumerate(expected):
            if num != heights[i]: 
                total += 1
        return total