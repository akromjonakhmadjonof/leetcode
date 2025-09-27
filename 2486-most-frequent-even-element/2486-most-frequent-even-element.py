class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = Counter(nums)
        freq = 0
        even_elem = -1
        for num, count in nums.items():
            if num % 2 == 0:
                if freq < count:
                    freq = count
                    even_elem = num
                elif freq == count:
                    even_elem = min(even_elem, num)
        return even_elem