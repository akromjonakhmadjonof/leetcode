class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}

        for i, num in enumerate(arr):
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen[num] = i
        return False