class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows,cols=len(grid),len(grid[0])
        minutes=0
        fresh_count=0
        from collections import deque
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_count+=1
        directions=[(0,1),(1,0),(-1,0),(0,-1)]    
        while queue and fresh_count>0:
            size=len(queue)
            minutes+=1
            for _ in range(size):
                cur_r,cur_c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=dr+cur_r,dc+cur_c
                    if(nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh_count-=1
                        queue.append((nr,nc))
                        
        return minutes if fresh_count==0 else -1

                    





        