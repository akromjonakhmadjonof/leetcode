class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, digit = coordinates
        col = ord(letter) - ord('a') + 1
        row = int(digit)
        return (col + row) % 2 == 1