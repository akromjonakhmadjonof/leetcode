class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answers = prices[:]
        stack = [ ]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                answers[index] = prices[index] - prices[i]
            stack.append(i)
        return answers