class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        nums.sort()
        total = sum(nums)
        pointer = 0
        while total % k:
            if nums[pointer] == 0:
                pointer += 1
            nums[pointer] -= 1
            total -= 1
            counter += 1
        return counter