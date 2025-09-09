from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)
        buckets = ["" for _ in range(n + 1)]

        for char, count in counter.items():
            buckets[count] += char * count
        return "".join(buckets[::-1])           
