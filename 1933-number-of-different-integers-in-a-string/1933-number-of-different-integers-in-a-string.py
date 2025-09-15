class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = list(word) # Turn into list to replace chars with space

        for i in range(len(word)):
            if word[i].isalpha():
                word[i] = " "
        nums = set() # Stores all nums without duplicates
        for item in set("".join(word).split(" ")):
            if item:
                nums.add(int(item))
                
        return len(nums)