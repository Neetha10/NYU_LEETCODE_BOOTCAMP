class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        connected_components=0
        visited=[]
        def dfs(node):
            visited.append(node)
            for v in graph[node]:
                if v not in visited:
                    dfs(v)
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected_components+=1
        return connected_components





        
        