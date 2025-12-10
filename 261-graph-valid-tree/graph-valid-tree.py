class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= n-1:
            return False
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[]
        def dfs(node):
            visited.append(node)
            for v in graph[node]:
                if v not in visited:
                    dfs(v)
        dfs(0)
        if len(visited)!=n:
            return False
        else:
            return True

    

        

        
        