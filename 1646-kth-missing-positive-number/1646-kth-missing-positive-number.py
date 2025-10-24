class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        max_num = arr[-1]
        arr = set(arr)
        for i in range(1, max_num):
            if i not in arr:
                k -= 1
                if k == 0:
                    return i
                

        return max_num + k
        
                
