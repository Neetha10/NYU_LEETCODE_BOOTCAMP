class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist=[float('inf')]* (n+1)
        dist[k]=0
        pq=[(0,k)]
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist[u]:
                continue
            for v,w in graph[u]:
                if dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
                    heapq.heappush(pq,(dist[v],v))
        return max(dist[1:]) if max(dist[1:])!=float('inf') else -1
        