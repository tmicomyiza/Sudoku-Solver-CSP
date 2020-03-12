from termcolor import colored
from csp import *
import time


#returns a list of values
def read_infile(name, variables):
    infile = open(name, 'r')
    data = infile.readlines()
    
    for var in data:
        temp = var.split()
        row = int(temp[0])
        col = int(temp[1])
        value = int(temp[2])

        variables[row][col] = value

    infile.close()
    return variables





#get input from the user
# returns a 2D list of integers
def get_input():
    num = 0

    lists_var = [[0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0]]

    status = input(colored("Do you want to use terminal or a file?" 
                                   + "(t: terminal or f:file) ","green"))
    

    if status.lower() == "t":
        num = int(input(colored("how man cells do you want to initialize? ", "green")))

        while num > 0:
            print(colored("select a cell to initialize. Enter informaiton in the " + 
                                                        "following order", "green"))

            data = input(colored("row col value (Note: row and col can (0-8) and value (1-9))",
                    "green")).split()


            row = int(data[0])
            col = int(data[1])
            value = int(data[2])

            lists_var[row][col] = value

            num -= 1

        return lists_var

    elif status.lower() == "f":
        print(colored("file must be formated in the following format:\n" 
            + "0 0 3\n"
            + "1 5 4\n", "green"))

        filename = input(colored("Enter filename: ", "green"))

        return read_infile(filename, lists_var)


    else:
        print(colored("Error: Invalid input", "red"))
        return






#DISPLAYS THE SOLVED SUDOKU IN THE GRID FORMAT
def display(board):
    for r in range(9):
        if r in[0,3,6]:
            print ("-------------------------------------------")
        for c in range(9):
            if c in [3,6]:
                print (' | ', board[r][c].value, ' ',end=' ')
            else:
                print (board[r][c].value, ' ',end=' ')
        print (end='\n')






#returns a list of initialized variables
def init_variables(array):
    lists_var = [[0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0]]

    for i in range(9):
        for j in range(9):
            var = Variable(i, j, array[i][j])
            lists_var[i][j] = var

    
    return lists_var






# Returns True if variable_to_check is valid input into board
# Checks horizontal, vertical, and box
# Does NOT actually input variable_to_check into board
# This still needs to be tested
def is_valid_input(empty_var, variable_to_check, board):
    row_loc = empty_var.row
    col_loc = empty_var.col

    # check horizontally
    for c in range(len(board[row_loc])):
        if (c == col_loc):
            continue
        if (board[row_loc][c].value == variable_to_check):
            return False

    # check vertically
    for r in range(len(board)):
        if (r == row_loc):
            continue
        if (board[r][col_loc].value == variable_to_check):
            return False

    # check box
    box_row = row_loc / 3
    box_col = col_loc / 3
    top_left_row = int(box_row) * 3
    top_left_col = int(box_col) * 3
    row_indecies_to_check = [top_left_row, top_left_row + 1, top_left_row + 2]
    col_indecies_to_check = [top_left_col, top_left_col + 1, top_left_col + 2]
    for r in row_indecies_to_check:
        for c in col_indecies_to_check:
            if (r == row_loc and c == col_loc):
                continue
            if (board[r][c].value == variable_to_check):
                return False

    return True





# Recursive Backtracking Solver
def Back_Tracking_Search(csp):
    if csp.complete(csp.board): # if assignment is complete then
        return True # return assignment

    # variable = Select-unassigned-variable(variables[csp], assignment, csp)
    empty_var = csp.find_empty(csp.board) 

    if empty_var == None:
        return False

    for domain_var in empty_var.domain: # for eachvalue in Order-Domain-Value(variable, assignment, csp) do
        valid = is_valid_input(empty_var, domain_var, csp.board)
        if valid: # if value is consistent with assignment given Constraints[csp] then
            csp.board[empty_var.row][empty_var.col].value = domain_var # add {variable = value} to assignment

            # result = Recursive-backtracking(assignment, csp) / if result is not failure then
            if Back_Tracking_Search(csp): 
                return True # return result
            ev = Variable(empty_var.row, empty_var.col, 0)
            csp.board[empty_var.row][empty_var.col] = ev # remove {variable = value} from assignment

    return False # return FAILURE







def main():

    # get inputs from user
    data = get_input()

    #create a 2D lists of variables
    board = init_variables(data)

    #create CPS instance to represent the board
    csp = CSP(board)

    #start timing
    starttimer = time.time()

    # solution is boolean value. True when there's a solution. False otherwise
    solution = Back_Tracking_Search(csp)

    #stop timer
    endtimer = time.time()

    if solution == True:
        print(colored("Congratulations! Sudoku solved", "blue"))
        display(csp.board)

        print(colored("\nThe algorithm took {0:0.1f} seconds to find solution"
                                        .format(endtimer - starttimer), "blue"))

    else:
        print(colored("Sudoku provided has no solution", "blue"))
        print(colored("\nThe algorithm took {0:0.1f} seconds to find solution"
                                        .format(endtimer - starttimer), "blue"))


if __name__ == "__main__":
    main()







