class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Map of morse alphabet of each char
        morse_code = {
            "a": ".-",    "b": "-...",  "c": "-.-.",  "d": "-..",
            "e": ".",     "f": "..-.",  "g": "--.",   "h": "....",
            "i": "..",    "j": ".---",  "k": "-.-",   "l": ".-..",
            "m": "--",    "n": "-.",    "o": "---",   "p": ".--.",
            "q": "--.-",  "r": ".-.",   "s": "...",   "t": "-",
            "u": "..-",   "v": "...-",  "w": ".--",   "x": "-..-",
            "y": "-.--",  "z": "--.."
        } 
        seen = set() # Stores words in morse format without duplicates
        for word in words:
            morse = "" # Regenerate the word in format alphabet
            for char in word:
                morse += morse_code[char]
            seen.add(morse)
        return len(list(seen))