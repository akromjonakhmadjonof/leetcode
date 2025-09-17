from collections import Counter
class Solution:
    def isFascinating(self, n: int) -> bool:
        final = Counter(str(n) + str(n * 2) + str(n * 3))
        for i in range(1, 10):
            if str(i) not in final or final[str(i)] != 1:
                return False
        return True
        
        