class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree=[0]*numCourses
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1
        queue=deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        topo_order=[]
        while queue:
            u=queue.popleft()
            topo_order.append(u)
            for v in graph[u]:
                in_degree[v]-=1
                if in_degree[v]==0:
                    queue.append(v)
        return topo_order if len(topo_order)==numCourses else []
        

        

        
        
