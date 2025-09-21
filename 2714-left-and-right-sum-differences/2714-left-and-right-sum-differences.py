class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        leftSum[0] = nums[0]
        rightSum = [0] * n
        rightSum[-1] = nums[-1]

        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i - 1] + nums[i]

        for i in range(len(nums) - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i]
        results = [0] * n
        for i in range(len(leftSum)):
            results[i] = abs(leftSum[i] - rightSum[i])
        return results        