class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0 # Initial Position
        visited = {(0, 0)}  # Start with origin visited
        
        # Moving the pointers according to direction by 1 unit
        for char in path:
            if char == "N":
                y += 1
            elif char == "S":
                y -= 1
            elif char == "E":
                x += 1
            elif char == "W":
                x -= 1

            if (x, y) in visited:
                return True
            visited.add((x, y))
        
        return False
