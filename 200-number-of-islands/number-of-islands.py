class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        island_count=0
        visited=set()
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        def explore_islands(r,c):
            stack=[(r,c)]
            while stack:
                cur_r,cur_c=stack.pop()
                for dr,dc in directions:
                    nr,nc=dr+cur_r,dc+cur_c
                    if(nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]=='1' and(nr,nc) not in visited):
                        stack.append((nr,nc))
                        visited.add((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]=='1' and (r,c) not in visited):
                    visited.add((r,c))
                    explore_islands(r,c)
                    island_count+=1
        return island_count
                

        