from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums) # Stores frequency of numbers
        results = [0, 0] # Stores the results
        for i in range(1, len(nums) + 1):
            # If number not in freq then it is missing one or if there are 2 of it then it is duplicate 
            if i not in freq:
                results[1] = i
            elif freq[i] == 2:
                results[0] = i
            
        return results