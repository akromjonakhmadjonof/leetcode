class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [] # Stores all chars of string

        for char in s:
            # If we encounter a char which is the same as previous one we are gonna pop the last element of the stack
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)