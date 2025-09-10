class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lenght of strings are not the same then it is not anagram
        if len(s) != len(t):
            return False

        
        s_count = Counter(s) # Stores frequcenies of each char in the string S
        t_count = Counter(t) # Stores frequcenies of each char in the string T

        # Iterate through the frequency list of the string S and compare to the string T
        for char, count in s_count.items():
            if t_count[char] != count:
                return False
        return True