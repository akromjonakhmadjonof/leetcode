class Solution:
    def buildGraph(self, paths:List[List[str]]):
        graph = {}
        for current, target in paths:
            if current not in graph:
                graph[current] = []
            if target not in graph:
                graph[target] = []
            graph[current].append(target)
        return graph
        
    def destCity(self, paths: List[List[str]]) -> str:
        # graph = self.buildGraph(paths)
        # def expand(current):
        #     if not graph[current]:
        #         return current
        #     for target in graph[current]:
        #         expand(target)
        #     return None
            
        # for current in graph.keys():
        #     check = expand(current)
        #     if check:
        #         return check

        targets = set()
        sources = set()

        for source, target in paths:
            targets.add(target)
            sources.add(source)
        return (targets - sources).pop()
        
                