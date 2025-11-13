class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char.isdigit() and stack[-1].isalpha():
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
