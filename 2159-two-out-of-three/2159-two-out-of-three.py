class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        results = [] # Stores results
        nums = list(set([*nums1, *nums2, *nums3])) # Gathers all numbers without duplicates
        nums1 = set(nums1) # Convert nums1 into set to search in O(1)
        nums2 = set(nums2) # Convert nums2 into set to search in O(1)
        nums3 = set(nums3) # Convert nums3 into set to search in O(1)

        for num in nums:
            if (num in nums1 and num in nums2) or(num in nums3 and num in nums2) or(num in nums1 and num in nums3):
                results.append(num)
        return results