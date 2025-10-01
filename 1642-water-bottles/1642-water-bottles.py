class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        current = numBottles

        while current >= numExchange:
            new_bottles = current // numExchange
            total += new_bottles
            current = new_bottles + (current % numExchange)

        return total
