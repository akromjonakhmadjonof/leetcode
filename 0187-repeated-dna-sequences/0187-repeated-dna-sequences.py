class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq = {}
        results = []
        for i in range(len(s) - 10):
            dna = s[i:i+10]
            freq[dna] = freq.get(dna, 0) + 1
        for dna, count in freq.items():
            if count > 1:
                results.append(dna)
        return results