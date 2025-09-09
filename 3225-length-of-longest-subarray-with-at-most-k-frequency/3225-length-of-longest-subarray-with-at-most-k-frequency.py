class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_len = 0 # Stores maximum lenght of longest subarray that fulfills requirements
        start = 0 # Pointer starting
        frequency = {} # Stores frequency of numbers in current window

        
        for end in range(len(nums)):
            current = nums[end]
            frequency[current] = frequency.get(current, 0) + 1
            # Checks if current number in the current window exceeds allowed frequency
            while frequency[current] > k:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == 0:
                    del frequency[nums[start]]
                start += 1
            # Updating maximum lenght
            max_len = max(max_len, end - start + 1)

        return max_len