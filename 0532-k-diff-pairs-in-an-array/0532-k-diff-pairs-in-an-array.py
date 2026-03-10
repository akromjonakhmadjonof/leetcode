class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        results = set()
        n = len(nums)
        

        for index, num in enumerate(nums):
            pointer = index + 1

            while pointer < n:
                if abs(nums[index] - nums[pointer]) == k:
                    results.add((nums[index], nums[pointer]))
                    pointer += 1
                elif abs(nums[index] - nums[pointer]) < k:
                    pointer += 1
                else:
                    break
        print(results)
        return len(results)
