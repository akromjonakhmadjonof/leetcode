from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        count = defaultdict(int)
        degree = 0
        min_len = float("inf")

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            count[x] += 1

            if count[x] > degree:
                degree = count[x]
                min_len = i - first[x] + 1
            elif count[x] == degree:
                min_len = min(min_len, i - first[x] + 1)

        return min_len
