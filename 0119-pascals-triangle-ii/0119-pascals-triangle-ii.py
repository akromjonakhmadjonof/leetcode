class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        levels = [[1], [1,1]]
        if rowIndex in levels:
            return levels[rowIndex]

        for i in range(2, rowIndex + 1):
            prev = levels[-1]
            new_curr = [1]
            for i in range(1, len(prev)):
                new_curr.append(prev[i] + prev[i - 1]) 
            new_curr.append(1)
            
            levels.append(new_curr)

        return levels[rowIndex]
            