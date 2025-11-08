class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(numbers, 1):
            if target - num in seen:
                return [seen[target-num], index]
            seen[num] = index