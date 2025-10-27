class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(target):
            digits = set(str(target))
            if "0" in digits:
                return False
            
            for digit in digits:
                if target % int(digit) != 0:
                    return False
            return True
        results = []
        for i in range(left, right + 1):
            if is_self_dividing(i):
                results.append(i)
        return results
