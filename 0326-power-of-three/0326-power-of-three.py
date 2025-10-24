class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return n / 3 == 1 or self.isPowerOfThree(n / 3)