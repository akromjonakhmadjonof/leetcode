from collections import Counter
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        freq = Counter(nums)

        # must contain exactly numbers 1..n
        for i in range(1, n):
            if freq[i] != 1:
                return False
        
        # n must appear exactly twice
        if freq[n] != 2:
            return False

        # ensure no other numbers exist
        if len(freq) != n:
            return False

        return True
