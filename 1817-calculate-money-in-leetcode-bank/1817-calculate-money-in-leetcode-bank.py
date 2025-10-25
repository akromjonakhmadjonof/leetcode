class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday_start = 1      # Deposit on the Monday of the current week
        today = monday_start  # Deposit for the current day

        for day in range(1, n + 1):
            total += today
            # If end of week, next day is a new Monday with +1 start; else just +1
            if day % 7 == 0:
                monday_start += 1
                today = monday_start
            else:
                today += 1
        return total
