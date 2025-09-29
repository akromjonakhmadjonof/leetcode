class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]

        for i, nums in enumerate(matrix):
            rows[i] = set(nums)
            for j, num in enumerate(nums):
                cols[j].add(num)

        expected = set(range(1, n + 1))
        for i in range(n):
            if rows[i] != expected or cols[i] != expected:
                return False
        return True
