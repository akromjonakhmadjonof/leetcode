class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
 
        results = [0] * n
        for i in range(n):
            start = max(0, i - nums[i])
            results[i] = sum(nums[start:i + 1])
        
        return sum(results)