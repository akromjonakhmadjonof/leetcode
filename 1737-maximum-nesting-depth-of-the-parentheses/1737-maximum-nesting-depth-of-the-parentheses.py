class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        current_depth = 0
        max_depth = current_depth
        for char in s:
            if char not in {"(", ")"}:
                continue
            elif char == "(":
                current_depth += 1
                stack.append(char)
            else:
                stack.pop()
                current_depth -= 1
            
            max_depth = max(max_depth, current_depth)
        return max_depth