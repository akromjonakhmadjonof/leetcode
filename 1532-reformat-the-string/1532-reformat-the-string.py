class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []

        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)
        
        if abs(len(digits) - len(letters)) > 1:
            return ""
        
        if len(digits) > len(letters):
            first, second = digits, letters
        else:
            first, second = letters, digits

        res = []
        for i in range(len(s)):
            if i % 2 == 0:
                res.append(first.pop(0))
            else:
                res.append(second.pop(0))
        return "".join(res)