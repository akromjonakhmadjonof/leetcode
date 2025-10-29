class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        results = [None] * 2
        nums = []
        flatten = lambda arr: nums.extend(arr)

        for item in grid:
            flatten(item)
        
        nums = Counter(nums)
        for i in range(1, pow(n, 2) + 1):
            if i not in nums:
                results[1] = i
            elif nums[i] == 2:
                results[0] = i

        return results