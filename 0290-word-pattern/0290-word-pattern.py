class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_to_p = {}
        p_to_s = {}
        if len(s.split()) != len(pattern):
            return False
            
        for sign, char in zip(pattern, s.split()):
            if sign in p_to_s and p_to_s[sign] != char:
                return False
            if char in s_to_p and s_to_p[char] != sign:
                return False
            
            s_to_p[char] = sign
            p_to_s[sign] = char
        return True