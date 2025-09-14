class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) # Find n
        nums = set(nums) # Turn array into set with uniqe elements to search in O(1)
        results = [] # Stores results
        for i in range(1, n + 1):
            if i not in nums:
                results.append(i)
        return results
            