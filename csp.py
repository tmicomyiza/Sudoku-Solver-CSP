# this is a class to represent csp
class  CSP:
    def __init__(self, board):
        self.board = board

    # finds the next empty variable to be assigned in the board
    def find_empty(self,board):
        for row in board:
            for variable in row:
                if variable.value == 0:
                    return variable


    #check if the board is solved
    def complete(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j].value == 0:
                    return False
                    
                if self.complete_helper(board, i, j) == False:
                    return False

        
        return True

    


    #helper function to evaluate completeness of a board
    def complete_helper(self,board, row, col):
        if len(board) == 0:
            return False

        value = board[row][col].value
        
        # check vertically
        for r in range(len(board)):
            if (r == row):
                continue
            if (board[r][col].value == value):
                return False
        
        # check horizontally
        for c in range(len(board[row])):
            if (c == col):
                continue
            if (board[row][c].value == value):
                return False
        
        # check 3x3 box
        box_row = row / 3
        box_col = col / 3
        top_left_row = int(box_row) * 3
        top_left_col = int(box_col) * 3
        row_indecies_to_check = [top_left_row, top_left_row + 1, top_left_row + 2]
        col_indecies_to_check = [top_left_col, top_left_col + 1, top_left_col + 2]
        for r in row_indecies_to_check:
            for c in col_indecies_to_check:
                if (r == row and c == col):
                    continue
                if (board[r][c].value == value):
                    return False
        
        return True 

        
        
class Variable:
    def __init__(self,row,col,value = 0):
        self.value = value
        self.row = row
        self.col = col
        self.domain = self.init_domain(value)

    #initializes domain of the variable
    def init_domain(self,value):
        domain = []
        for i in range(1,10):
            if i != value:
                domain.append(i)

        return domain






