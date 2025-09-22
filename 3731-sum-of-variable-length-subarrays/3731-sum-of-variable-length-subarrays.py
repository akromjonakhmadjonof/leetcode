class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n + 1):
            prefix.append(prefix[-1] + nums[i - 1])

        result = 0
        for i in range(n):
            start = max(0, i - nums[i])
            result += prefix[i+1] - prefix[start]
        
        return result