class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        obj = {} # Stores strings in list1 with indexes 
        results = [] # Stores results
        min_sum = float("inf") # Stores minimum sum of the same string indexes

        for index, string in enumerate(list1):
            obj[string] = index

        for index, string in enumerate(list2):
            if string in obj:
                index_sum = index + obj[string]
                # If index_sum is less than min_sum we have to clear results otherwise if equals we have to add and skip others
                if index_sum < min_sum:
                    results.clear()
                    results.append(string)
                    min_sum = index_sum
                elif index_sum == min_sum:
                    results.append(string)
                
        return results