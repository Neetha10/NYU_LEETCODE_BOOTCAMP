class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visited=[[False]*cols for i in range (rows)]
       

        def backtrack(r,c,index):
            if index==len(word):
                return True

            if(r<0 or c<0 or r>=rows or c>=cols or visited[r][c] or board[r][c] != word[index] ):
                return False
            visited[r][c]=True

            found= (backtrack(r+1,c,index+1) or backtrack(r-1,c,index+1) or backtrack(r,c+1,index+1) or backtrack(r,c-1,index+1))

            visited[r][c]=False
            return found




        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True
        return False
            
            

            
        