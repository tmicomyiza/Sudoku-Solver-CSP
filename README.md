# SudokuSolver-CSP
## Jamie Weiss and Mico Micomyiza Theogene


## DESCRIPTION
Sudoku Solver using Constraints Satisfaction Problems. We use back tracking search algorithm to solve sudoku.

    #Variables
        Each cell on the Sudoku board is variable. 
        There are 81 variable in total becaue the board is 9 X 9 square

    #Domain:
        Additionally, each variable has domain of {1,2,3,4,5,6,7,8,9}

    # Constraints
        1. a value cannot redudant in a row
        2. a value cannot be redudant in a column
        3. a value cannot be redudant in 3 X 3 sqaure box


## PYTHON FILES
csp.py contains the models used.
sodoku.py contains the implementation and main code to solve sudoku provided


## REQUIREMENTS

Minimum Python requirements (earlier versions may work but have not been tested):

* Python 3 (3.7.6)
* termcolor module for printing


## HOW TO RUN IT

`python3 sudoku.py`


after running the above command,
you will receive guidance on the use of the program on terminal.

    1. If you want, you can use terminal to insert inputs

    2. You can create an input file with the following format:
        row col value newline
        

        Note: these are values to help initialize fixed cells on sudoku
## PROVIDED TEST FILES
    easy.txt and harder.txt as test files

## Note: You cannot provide the filename name as parameter when you launch the program.




