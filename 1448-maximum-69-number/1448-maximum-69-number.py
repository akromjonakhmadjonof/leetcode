class Solution:
    def maximum69Number (self, num: int) -> int:
        replacable = {"9": "6", "6": "9"}
        num = str(num)
        max_number = 0
        for i, digit in enumerate(num):
            new_digit = replacable[digit]
            max_number = max(max_number, int(num[:i] + new_digit + num[i + 1:]), int(num))
        return max_number