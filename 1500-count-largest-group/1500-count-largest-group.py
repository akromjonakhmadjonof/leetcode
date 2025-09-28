class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digits_sum(num):
            return sum(int(digit) for digit in str(num))
        
        groups = {}
        
        # Count numbers in each digit-sum group
        for i in range(1, n + 1):
            digit_sum = digits_sum(i)
            groups[digit_sum] = groups.get(digit_sum, 0) + 1
        
        # Find the largest group size
        max_size = max(groups.values())
        
        # Count how many groups have that max size
        return sum(1 for size in groups.values() if size == max_size)
