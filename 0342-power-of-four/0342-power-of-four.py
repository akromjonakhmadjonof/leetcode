class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        current = n
        while current % 4 == 0:
            current //= 4

        return current == 1
