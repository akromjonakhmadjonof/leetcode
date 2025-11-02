class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        n = min(n1, n2)
        divisor = ""
        for i in range(1, n + 1):
            l_divisor = str1[:i]
            n_divisor = len(l_divisor)
            count1, count2 =  n1 // n_divisor, n2 // n_divisor
            if l_divisor * count1 == str1 and l_divisor * count2 == str2:
                divisor = l_divisor
                
        return divisor