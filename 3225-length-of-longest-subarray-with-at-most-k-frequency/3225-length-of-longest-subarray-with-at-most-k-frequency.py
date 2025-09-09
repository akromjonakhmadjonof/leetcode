class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_len = 0
        start = 0
        frequency = {}

        for end in range(len(nums)):
            current = nums[end]
            frequency[current] = frequency.get(current, 0) + 1

            while frequency[current] > k:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == 0:
                    del frequency[nums[start]]
                start += 1
            max_len = max(max_len, end - start + 1)

        return max_len