class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        final = {}

        for item in items1:
            key, value = item
            if key in final:
                final[key] += value
            else:
                final[key] = value
        
        for item in items2:
            key, value = item
            if key in final:
                final[key] += value
            else:
                final[key] = value
        results = []
        for key, value in final.items():
            results.append([key, value])
        return sorted(results)