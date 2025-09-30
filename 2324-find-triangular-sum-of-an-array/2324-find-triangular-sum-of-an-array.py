from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def helper(numbers):
            if len(numbers) == 1:
                return numbers[0]
            results = []
            for i in range(1, len(numbers)):
                results.append((numbers[i] + numbers[i-1]) % 10)
            return helper(results)
        return helper(nums)
