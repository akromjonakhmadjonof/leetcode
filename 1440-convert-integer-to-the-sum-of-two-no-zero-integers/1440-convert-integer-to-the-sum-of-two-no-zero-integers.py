class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        has_zero = lambda num: "0" in str(num)

        for i in range(1, n // 2 + 1):
            if not has_zero(i) and not has_zero(n - i):
                return [i, n - i]
            
