class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        levels = [[1],[1, 1]]
        for level in range(3, numRows + 1):
            prev_level = levels[-1]
            new_level = [1]
            for i in range(1, len(prev_level)):
                new_level.append(prev_level[i] + prev_level[i - 1])
            new_level.append(1)
            levels.append(new_level)
        return list(levels)