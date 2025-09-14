from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = [] # Stores results
        nums1_counter = Counter(nums1) # Stores frequencies of elements in nums1
        nums2_counter = Counter(nums2) # # Stores frequencies of elements in nums2

        for num, count in nums1_counter.items():
            if num in nums2_counter:
                # If number exists in both arrays adds to the results with minimum number
                results.extend([num] * min(nums2_counter[num], count)) 
        return results