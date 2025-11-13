class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_cons = count
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_cons = max(max_cons, count)
                count = 0
        max_cons = max(max_cons, count)
        return max_cons
            
                