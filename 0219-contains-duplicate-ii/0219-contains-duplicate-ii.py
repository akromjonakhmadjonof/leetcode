class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {} # Stores indices 

        for i, num in enumerate(nums):
            # If there is no num in indices just push
            if num not in indices:
                indices[num] = i
            else:
                # If we have the index of previous occurance of current number check distance between them is less then or equal to k
                # Otherwise update index
                if abs(indices[num] - i) <= k:
                    return True
                else:
                    indices[num] = i
        # At the end if we cannot find pair of numbers that satisfy the requirement we have to return False
        return False
        