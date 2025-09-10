class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(x: str) -> str:
            stack = []
            # When we encounter # we have to delete the previous element otherwise add to stack
            for ch in x:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return "".join(stack)
        # Comparing two states after going through process
        return process(s) == process(t)