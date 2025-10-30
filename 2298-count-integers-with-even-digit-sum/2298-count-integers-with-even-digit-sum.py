class Solution:
    def countEven(self, num: int) -> int:
        check = lambda x: sum([int(i) for i in list(str(x))])
        count = 0
        for i in range(1, num + 1):
            if check(i) % 2 == 0:
                count += 1
        return count