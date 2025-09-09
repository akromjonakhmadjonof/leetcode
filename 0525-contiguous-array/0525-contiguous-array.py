class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        results = {} # Stores in which position what value we had 
        results[0] = -1 # Initially before the earliest element we have total value of 0 which is at -1
        max_len = 0 # Store maximum lenght of subarray
        total = 0 # Stores all numbers +1 if num in nums is 1 else -1
        
        # Iterates through the list
        for i in range(len(nums)):
            total += -1 if not nums[i] else 1
            
            if total in results:
                max_len = max(max_len, i - results[total])
            else:
                results[total] = i

        return max_len

            