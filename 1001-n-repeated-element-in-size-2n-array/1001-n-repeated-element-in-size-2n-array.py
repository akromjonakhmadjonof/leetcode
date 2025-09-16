from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums = Counter(nums)

        for num, count in nums.items():
            if count != 1:
                return num
        