class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                curr_len = 1
                while current + 1 in nums:
                    current += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        
        return max_len