class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        freq = Counter(nums)
        for i in nums:
            if freq[i - diff] and freq[i + diff]:
                counter += 1
        return counter
