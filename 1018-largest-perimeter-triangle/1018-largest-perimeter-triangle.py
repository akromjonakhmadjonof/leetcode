class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()  # O(n log n)
        # Check consecutive triplets from largest to smallest
        for i in range(len(nums) - 1, 1, -1):
            a, b, c = nums[i-2], nums[i-1], nums[i]  # c is largest
            if a + b > c:             # only need this check
                return a + b + c      # first valid is maximal perimeter
        return 0