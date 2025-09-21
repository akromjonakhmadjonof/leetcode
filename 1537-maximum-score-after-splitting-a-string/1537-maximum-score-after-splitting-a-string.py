class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros = [0] * n
        ones = [0] * n

        # prefix count of zeros
        zeros[0] = 1 if s[0] == "0" else 0
        for i in range(1, n):
            zeros[i] = zeros[i - 1] + (1 if s[i] == "0" else 0)

        # suffix count of ones
        ones[-1] = 1 if s[-1] == "1" else 0
        for i in range(n - 2, -1, -1):
            ones[i] = ones[i + 1] + (1 if s[i] == "1" else 0)

        max_score = 0
        # split must happen between [0 .. n-2]
        for i in range(n - 1):
            max_score = max(max_score, zeros[i] + ones[i + 1])
        return max_score
