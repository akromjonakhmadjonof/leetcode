class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        results = []
        n = len(arr)
        centre = arr[(n-1) // 2]
        left, right = 0, n - 1
    
        while left <= right:
            if len(results) == k:
                return results
        
            if abs(arr[left] - centre) > abs(arr[right] - centre):
                results.append(arr[left])
                left += 1
            else: 
                results.append(arr[right])
                right -= 1
        return results

