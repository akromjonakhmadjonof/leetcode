from collections import Counter
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersections = set(nums[0])
        for i in range(1, len(nums)):
            arr = nums[i]
            intersections = intersections & set(arr)
        return sorted(list(intersections))