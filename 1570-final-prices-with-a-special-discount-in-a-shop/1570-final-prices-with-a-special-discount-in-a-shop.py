class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answers = prices[:] # We are gonna copy prices list as default returning answer
        stack = []

        for i in range(len(prices)):
            # We are gonna check if the last item in stack is greater then current element 
            # If yes then we have to apply discount if not we have to go on
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                answers[index] = prices[index] - prices[i]
            stack.append(i)
        
        return answers