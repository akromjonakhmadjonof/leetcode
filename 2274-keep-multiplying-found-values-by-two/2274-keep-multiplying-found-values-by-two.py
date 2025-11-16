class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in set(nums):
            return original
        return self.findFinalValue(nums, original * 2)