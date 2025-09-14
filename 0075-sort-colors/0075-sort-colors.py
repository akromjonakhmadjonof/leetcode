from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = Counter(nums) # Stores frequency of numbers
        nums[:] = []

        for i in range(3):
            answer = [i] * counter[i]
            nums.extend(answer)
        