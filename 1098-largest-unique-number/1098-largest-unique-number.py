from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        uniqe_large = -1
        for num, count in counts.items():
            if count == 1:
                uniqe_large = max(uniqe_large, num)
        return uniqe_large
            