class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        max_num = max(nums)
        # iterate only through multiples of k
        for i in range(k, max_num + 1, k):
            if i not in s:
                return i
        return ((max_num // k) + 1) * k
