class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows=len(rooms)
        cols=len(rooms[0])
        visited=set()
        queue=deque()

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col]==0:
                    queue.append((row,col))
                    visited.add((row,col))
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc]==2147483647:
                    rooms[nr][nc]=rooms[r][c]+1
                    queue.append((nr,nc))


           
        


        
                    



        
        """
        Do not return anything, modify rooms in-place instead.
        """
        