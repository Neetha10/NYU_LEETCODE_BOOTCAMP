class Solution:
    def check(self,row,col,heights,ocean):
        rows=len(heights)
        cols=len(heights[0])
        ocean[row][col]=True
        
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for dr,dc in directions:
            nr=row+dr
            nc=col+dc
            if 0<=nr<rows and 0<=nc<cols and not ocean[nr][nc] and heights[nr][nc]>=heights[row][col]:
                self.check(nr,nc,heights,ocean)
        return
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result=[]
        rows=len(heights)
        cols=len(heights[0])
        pac=[[False for j in range(cols)] for i in range(rows)]
        atl=[[False for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            self.check(i,0,heights,pac)
            self.check(i,cols-1,heights,atl)
        for i in range(cols):
            self.check(0,i,heights,pac)
            self.check(rows-1,i,heights,atl)

        for r in range (rows):
            for c in range(cols):
                if atl[r][c] and pac[r][c]:
                    result.append([r,c])
        return result