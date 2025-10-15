class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        results = []
        one_third_of_n = n / 3

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, count in freq.items():
            if count > one_third_of_n:
                results.append(num)
        return results