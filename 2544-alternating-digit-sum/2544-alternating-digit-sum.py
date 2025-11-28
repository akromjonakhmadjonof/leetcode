class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        digits = [(int(n[0]), "+")]
        for i in range(1, len(n)):
            if digits[-1][-1] == "+":
                digits.append((int(n[i]), "-"))
            else:
                digits.append((int(n[i]), "+"))
        total = 0

        for num,sign in digits:
            if sign == "+":
                total += num
            else:
                total -= num
        return total