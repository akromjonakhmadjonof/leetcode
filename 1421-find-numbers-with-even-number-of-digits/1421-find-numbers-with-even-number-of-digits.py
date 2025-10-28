class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digit_count = lambda num: len(str(num))
        count = 0
        for num in nums:
            if digit_count(num) % 2 == 0:
                count += 1
        return count
