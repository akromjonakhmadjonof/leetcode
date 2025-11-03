class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(x: int) -> bool:
            sum_digits = lambda num: sum([int(digit) for digit in num])
            x = str(x)
            if len(x) % 2 != 0:
                return False
            half = len(x) // 2
            first = x[:half]
            second = x[half:]
            return sum_digits(first) == sum_digits(second)
        count = 0
        for i in range(low, high + 1):
            if is_symmetric(i):
                count += 1
        return count