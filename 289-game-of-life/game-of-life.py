class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        m=len(board)
        n=len(board[0])
        copy=[]
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(board[i][j])
            copy.append(row)
            
        for i in range(m):
            for j in range(n):
                live_neighbours=0
                for neighbour in neighbours:
                    neighbour_row=(i+neighbour[0])
                    neighbour_col=(j+neighbour[1])
                    if((neighbour_row>=0 and neighbour_row <m) and (neighbour_col>=0 and neighbour_col <n) and (copy[neighbour_row][neighbour_col]==1)):
                        live_neighbours+=1
                if copy[i][j]==1 and live_neighbours<2:
                            board[i][j]=0
                elif copy[i][j]==1 and (live_neighbours ==2 or live_neighbours==3):
                            board[i][j]=1
                elif copy[i][j]==1 and live_neighbours>3:
                            board[i][j]=0
                elif copy[i][j]==0 and live_neighbours==3:
                            board[i][j]=1
                            
                    
                    

                    




    
        