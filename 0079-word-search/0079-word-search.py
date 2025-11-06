class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        y_limit, x_limit = len(board), len(board[0])
        visited = set()
        def dfs(x, y, i):
            if i == len(word):
                return True
            if (
                x < 0 or y < 0 or
                x >= y_limit or y >= x_limit or
                (x, y) in visited or
                board[x][y] != word[i]
            ):
                return False

            visited.add((x, y))
            found = (
                dfs(x + 1, y, i + 1) or
                dfs(x - 1, y, i + 1) or
                dfs(x, y + 1, i + 1) or
                dfs(x, y - 1, i + 1)
            )
            visited.remove((x, y))
            return found

        for x in range(y_limit):
            for y in range(x_limit):
                if dfs(x, y, 0):
                    return True
        return False