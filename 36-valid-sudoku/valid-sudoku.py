class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen=set()
            for j in range(9):
                val=board[i][j]
                if val !='.':
                    if val in seen:
                        return False
                    seen.add(val)
        for j in range(9):
            seen=set()
            for i in range(9):
                val=board[i][j]
                if val!='.':
                    if val in seen:
                        return False
                    seen.add(val)
        for start_row in [0,3,6]:
            for start_col in [0,3,6]:
                seen=set()
                for i in range(3):
                    for j in range(3):
                        val_row=start_row+i
                        val_col=start_col+j
                        val=board[val_row][val_col]
                        if val!='.':
                            if val in seen:
                                return False
                            seen.add(val)
        return True
                        
                            
                



               
                

     
               
        



     
        