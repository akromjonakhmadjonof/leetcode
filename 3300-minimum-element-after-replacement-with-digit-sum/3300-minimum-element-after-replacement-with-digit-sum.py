class Solution:
    def minElement(self, nums: List[int]) -> int:
        digit_sum = lambda x: sum(int(digit) for digit in str(x))
        minimum = float("inf")
        for num in nums:
            minimum = min(digit_sum(num), minimum) 
            
        return minimum