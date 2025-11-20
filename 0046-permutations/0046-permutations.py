class Solution:
    def backtracking(self, nums, used, current, results):
        if len(current) == len(nums):
            results.append(current[:])
            return
        for index, num in enumerate(nums):
            if used[index] == True:
                continue
            used[index] = True
            current.append(num)
            self.backtracking(nums, used, current, results)
            current.pop()
            used[index] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        used = [False] * n
        current = []
             

        self.backtracking(nums, used, current, results)
        return results