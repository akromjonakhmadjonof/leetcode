from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Counting numbers' frequenc
        counts = Counter(nums).values()
        
        # Bucketing
        buckets = [0] * (len(nums) + 1)
        for c in counts:
            buckets[c] += 1
        for f in range(len(nums), 0, -1):
            if buckets[f]:
                return f * buckets[f]
        return 0 