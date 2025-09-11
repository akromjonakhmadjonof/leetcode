class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] # Tracks portions of path 
        for portion in path.split('/'):
            # If portion is .. we have to go back previous directory which means we have to pop last portion
            if portion == "..":
                if stack:
                    stack.pop()
            # If portion is . or nothing we have to skip
            elif portion  == "." or not portion:
                continue
            # Otherwise we have to just append the portion to path
            else:
                stack.append(portion)
        # Reformating the stack into single path
        return "/" + "/".join(stack)