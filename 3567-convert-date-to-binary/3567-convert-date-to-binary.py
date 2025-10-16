class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, date, month = [int(num) for num in date.split("-")]
        return f"{bin(year)[2:]}-{bin(date)[2:]}-{bin(month)[2:]}"