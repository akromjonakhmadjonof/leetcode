class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        for ch in s:
            if ch == '(':
                depth += 1
                if depth > 1:
                    result.append(ch)
            else:  
                depth -= 1
                if depth > 0:
                    result.append(ch)
        return "".join(result)