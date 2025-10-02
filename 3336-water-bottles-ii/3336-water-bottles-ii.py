class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        drunk = 0

        while full > 0:
            
            drunk += full
            empty += full
            full = 0

           
            if empty >= numExchange:
                empty -= numExchange
                full += 1
                numExchange += 1
            else:
                break

        return drunk