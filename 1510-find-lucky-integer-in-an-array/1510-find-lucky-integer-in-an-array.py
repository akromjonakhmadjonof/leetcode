from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr) # Stores numbers' frequencies
        luckies = -1  # Stores the luckiest number
        # Iterates through the frequency list
        for num, count in counter.items():
            if num == count:
                luckies = max(luckies, num)
        return luckies
                