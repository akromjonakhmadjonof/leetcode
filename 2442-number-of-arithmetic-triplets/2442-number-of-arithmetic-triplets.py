class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        seen = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i < j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        seen.add((nums[i], nums[j], nums[k]))

        return len(seen)


