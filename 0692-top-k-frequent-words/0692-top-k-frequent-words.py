class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        words = Counter(words)
        
        buckets = [[] for _ in range(n)]

        for word, count in words.items():
            buckets[count].append(word)
        results = []

        for i in range(n - 1, -1, -1):
            bucket = sorted(buckets[i])
            for word in bucket:
                results.append(word)
                k -= 1
                if  k == 0:
                    return results