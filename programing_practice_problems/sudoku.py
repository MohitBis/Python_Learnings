from itertools import product

def solve_sudoku(puzzle):
    for (row,col) in product(range(0,9), repeat=2):
        if puzzle[row][col] == 0:
            for num in range(0,9):
                allowed = True
                for i in range(0,9):
                    if (puzzle[i][col] == num) or (puzzle[row][i] == num):
                        allowed = False; break
                for (i,j) in product(range(0,3), repeat=2):
                    if puzzle[row-row%3+1][col-col%3+j] == num:
                        allowed = False
                if allowed:
                    puzzle[row][col] = num
                    # trial = solve_sudoku(puzzle)
                    # if trial == solve_sudoku(puzzle):
                    #     puzzle[row][col] = 0
                    # else:
                    #     return trial
            return False
    return puzzle

def print_sudoku(puzzle):
    puzzle = [["*" if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0,9):
        if ((row % 3 == 0) and (row != 0)):
            print("-"*33)
        for col in range(0,9):
            if ((col%3 == 0) and (col != 0)):
                print("|", end=" ")
            print("",puzzle[row][col],"",end="")
        print()
    print()

puzzel=[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
print_sudoku(puzzel)
print(solve_sudoku(puzzel))




