from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        
        for num, count in nums.items():
            if count > 2:
                return False
        return True
