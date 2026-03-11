class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives, negatives = [], []
        result = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        for i in range(len(positives)):
            result.append(positives[i]) 
            result.append(negatives[i]) 
        return result