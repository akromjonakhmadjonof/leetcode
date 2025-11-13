class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        subs = {"B": "A", "D": "C"}
        for char in s:
            if stack and char in subs and stack[-1] in subs[char]:
                stack.pop()
            else:
                stack.append(char) 
        return len(stack)