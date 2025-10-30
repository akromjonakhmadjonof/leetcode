class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        largest = nums[-1]
        smallest = nums[0]
        print(largest, smallest)
        if largest % smallest == 0:
            return smallest
        
        for i in range(smallest - 1, 0, -1):
            if smallest % i == 0 and largest % i == 0:
                return  i
        return -1