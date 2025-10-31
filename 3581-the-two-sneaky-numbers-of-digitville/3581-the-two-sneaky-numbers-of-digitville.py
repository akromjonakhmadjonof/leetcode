class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        results = []
        for num, count in freq.items():
            if count == 2:
                results.append(num)
        return results
