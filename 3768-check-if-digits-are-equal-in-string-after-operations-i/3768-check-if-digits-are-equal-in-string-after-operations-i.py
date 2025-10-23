class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            result = []
            for i in range(len(s) - 1):
                digit1 = int(s[i])
                digit2 = int(s[i + 1])
                result.append(str((digit1 + digit2) % 10))
            s = "".join(result)    
        return s[0] == s[1]