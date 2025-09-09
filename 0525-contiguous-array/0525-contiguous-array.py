class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        results = {}
        results[0] = -1
        max_len = 0
        total = 0
        
        for i in range(len(nums)):
            total += -1 if not nums[i] else 1
            
            if total in results:
                max_len = max(max_len, i - results[total])
            else:
                results[total] = i

        return max_len

            