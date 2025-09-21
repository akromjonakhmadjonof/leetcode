class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] == nums[right] *  -1:
                return abs(nums[right])
            elif abs(nums[left]) > abs(nums[right]):
                left += 1
            else:
                right -= 1
        return -1