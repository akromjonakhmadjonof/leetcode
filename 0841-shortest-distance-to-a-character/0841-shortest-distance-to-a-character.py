class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        char_indexes = set()
        for index, char in enumerate(s):
            if char == c:
                char_indexes.add(index)
        
        def get_nearest(index):
            distances = []

            for i in char_indexes:
                distances.append(abs(i - index))
            return min(distances)
        
        results = [0] * len(s)
        for index, char in enumerate(s):
            distance = get_nearest(index)
            results[index] = distance
        return results