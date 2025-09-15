from collections import Counter
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        nums = Counter(nums) # Stores the frequency of each num in nums
        # Instead of algo to find if num is prime it is more optimal to hardcode since the nums.lenght is less than or equal to 100
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97} 
        for num, count in nums.items():
            if count in primes:
                return True
        return False