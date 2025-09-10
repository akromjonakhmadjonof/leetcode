class Solution:
    def makeGood(self, s: str) -> str:
        stack = [] # Stores all chars of string
        for char in s:
            # If the last element of stack is lower and current element is upper it removes both and vice-versa
            if stack and ((stack[-1].islower() and char.isupper() and stack[-1] == char.lower()) or
                          (stack[-1].isupper() and char.islower() and stack[-1].lower() == char)):
                stack.pop()
            else:
                stack.append(char) # Pushes the char to the end
        return "".join(stack)
