class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a","e","i","o","u"}
        sentence = sentence.split(" ")
        for index, word in enumerate(sentence):
            first = word[0]
            made_up_word = ""
            if first.lower() in vowels:
                made_up_word = word + "ma"
            else:
                made_up_word = word[1:] + first + "ma"
            made_up_word += "a" * (index + 1)
            sentence[index] = made_up_word
        return " ".join(sentence)