from collections import Counter
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        # Check if n is prime
        def check(n):
            if n == 1:
                return False
            for i in range(2, n//2 + 1):
                if n % i == 0:
                    return False
            return True

        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        for i in freq.values():
            if check(i) == True:
                return True
        return False