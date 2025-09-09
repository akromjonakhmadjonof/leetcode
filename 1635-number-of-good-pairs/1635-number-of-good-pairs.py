from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums) # Store the frequency of all numbers
        total = 0 # Counts how many good pairs are there
        # Iterate through frequencies to calculate good pairs number 
        for number, count in counter.items():
            total += (count * (count - 1)) // 2

        return total