from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) # Stores the frequency of numbers
        seen = set() # Stores seen frequencies

        # Iterates the counter and checks if all the number of frequencies of numbers are not the same
        for num, count in counter.items():
            if count in seen:
                return False
            seen.add(count)
        return True
