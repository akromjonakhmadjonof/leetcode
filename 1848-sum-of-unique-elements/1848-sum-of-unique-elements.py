from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = 0
        for num, count in counter.items():
            if count == 1:
                total += num
        return total