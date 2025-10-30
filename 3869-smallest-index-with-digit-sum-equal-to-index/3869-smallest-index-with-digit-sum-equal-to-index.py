class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        digit_sum = lambda x: sum([int(i) for i in str(x)])

        for index, num in enumerate(nums):
            if index == digit_sum(num):
                return index
        return  -1