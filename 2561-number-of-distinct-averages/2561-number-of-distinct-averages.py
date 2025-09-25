class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()
        left, right = 0, len(nums) - 1
        while left < right:
            num1 = nums[left]
            num2 = nums[right]
            averages.add((num1+num2) / 2)
            left += 1
            right -= 1
        return len(averages)