class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                if not removed:
                    removed = True
                else:
                    return False
            
            if i > 1 and nums[i] <= nums[i - 2]:
                nums[i] = nums[i - 1]
        return True