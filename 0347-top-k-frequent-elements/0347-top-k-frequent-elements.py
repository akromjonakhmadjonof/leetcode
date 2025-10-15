from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        buckets = [[] for _ in range(n + 1)]
        results = []

        for num, count in freq.items():
            buckets[count].append(num)

        for i in range(n, -1, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results
