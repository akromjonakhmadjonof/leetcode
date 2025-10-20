class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)
        n = len(board)
        for r in range(n):
            for c in range(n):
                num = board[r][c]
                position = (r // 3, c // 3)
                if num == ".":
                    continue
                
                if num in rows[r] or num in cols[c] or num in grids[position]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                grids[position].add(num)
        return True
                