class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        element_sum = 0
        d_sum = lambda x: sum([int(digit) for digit in str(x)]) 
        for num in nums:
            element_sum += num
            digit_sum += d_sum(num)
        return abs(digit_sum - element_sum)