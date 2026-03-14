class Solution:
    def countVowels(self, word):
        freq = Counter(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        for char, num in freq.items():
            if char in vowels:
                count += num
        return count

    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        target = 0

        for i, word in enumerate(s):
            if i == 0:
                target = self.countVowels(word)
            elif self.countVowels(word) == target:
                s[i] = s[i][::-1]
        return " ".join(s)