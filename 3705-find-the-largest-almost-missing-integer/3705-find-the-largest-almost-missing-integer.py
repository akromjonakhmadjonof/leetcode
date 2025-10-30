class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarrays = []
        n = len(nums)
        counts = set(nums)
        results = []
        for i in range(n - k + 1):
            subarrays.append(set(nums[i:i+k]))
        
        for num in counts:
            appeared = 0
            for subarray in subarrays:
                if num in subarray:
                    appeared += 1
                
            if appeared == 1:
                results.append(num)
        return  max(results) if results else -1
                    