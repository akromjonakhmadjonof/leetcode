class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total_sum = 0

        for i in range(1, n + 1):
            if any([i % 3 == 0, i % 7 == 0, i % 5 == 0]):
                total_sum += i
        return total_sum