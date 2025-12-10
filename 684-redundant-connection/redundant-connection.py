class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
       

        def dfs(start,target):
            if start==target:
                return True
            visited.append(start)
            for neighbours in graph[start]:
                if neighbours not in visited:
                    if dfs(neighbours,target):
                        return True
            return False
            
            
           
        for u,v in edges:
            visited=[]
            if dfs(u,v):
               return [u,v]
            else:
                graph[u].append(v)
                graph[v].append(u)

