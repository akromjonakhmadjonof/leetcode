class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = float("-inf")
        for i in range(n):
            for j in range(n):
                if i != j:
                    max_sum = max(max_sum, (nums[i] - 1) * (nums[j] - 1))
        return max_sum