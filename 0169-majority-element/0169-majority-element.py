class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums) # Stores frequencies of elements
        majority_element = 0 # Stores majority element 
        element_count = 0 # Stores majority element index
        for char, count in counter.items():
            if count > element_count:
                element_count = count
                majority_element = char
        return majority_element