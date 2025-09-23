class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
            
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]
        
        count = 0

        for i in range(n - 1):
            if abs(prefix[i] - suffix[i + 1]) % 2 == 0:
                count +=1 
        return count