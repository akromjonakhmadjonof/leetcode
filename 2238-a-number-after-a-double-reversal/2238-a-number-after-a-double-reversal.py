class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse = lambda x: int(str(x)[::-1])
        if reverse(reverse(num)) == num:
            return True
        return False
        