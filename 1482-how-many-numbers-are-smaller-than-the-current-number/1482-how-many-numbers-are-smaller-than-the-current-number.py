class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nsorted = sorted(nums,reverse=True)
        memo = {}
        n = len(nums)
        for index, num in enumerate(nsorted):
            memo[num] =  n - index - 1
        answer = [0] * n
        for i in range(n):
            answer[i] = memo[nums[i]]
        return answer