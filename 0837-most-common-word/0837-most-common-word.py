from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned) # Turn list into set for O(1) search
        remove_chars = "!?',;." # Chars should be removed
        table = str.maketrans({c: " " for c in remove_chars})
        paragraph = paragraph.translate(table).lower() # Remove chars

        freq = {} # Stores frequencies of words in paragraph
        max_count, common_word = 0, None # Stores max number of common word and itself
        
    
        for word in paragraph.split():
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1
                if freq[word] > max_count:
                    max_count = freq[word]
                    common_word = word
        
        return common_word
