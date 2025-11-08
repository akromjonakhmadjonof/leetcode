class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            result = []
            i = j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1
            result.extend(arr1[i:])
            result.extend(arr2[j:])
            return result

        def mergeSort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            mid = n // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)

        return mergeSort(nums)
