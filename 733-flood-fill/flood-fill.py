class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        original_color=image[sr][sc]
        if original_color==color:
            return image
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        stack=[(sr,sc)]
        image[sr][sc]=color
        while stack:
            cur_r,cur_c=stack.pop()
            for dr,dc in directions:
                nr,nc=cur_r+dr,cur_c+dc
                if(nr>=0 and nr<rows and nc>=0 and nc<cols and image[nr][nc]==original_color):
                    image[nr][nc]=color
                    stack.append((nr,nc))
        return image















        

        
        
        