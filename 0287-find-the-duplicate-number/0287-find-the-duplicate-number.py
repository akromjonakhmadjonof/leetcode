class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        previous = None
        for i in range(n):
            if nums[i] == previous:
                return nums[i]
            previous = nums[i]