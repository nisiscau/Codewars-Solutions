def valid(puzzle, num, pos):

    # Check if number is valid in row
    for i in range(len(puzzle[0])):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    # Check if number is valid in column
    for i in range(len(puzzle)):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    # Check if number is valid in square
    square_x = pos[1] // 3
    square_y = pos[0] // 3

    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x*3, square_x*3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False

    return True

def incomplete(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return i, j  # row, column

    return None


def sudoku(puzzle):
    find = incomplete(puzzle)
    if not find:  # if find is None or False
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(puzzle, num, (row, col)):
            puzzle[row][col] = num

            if sudoku(puzzle):
                return puzzle

            puzzle[row][col] = 0

    return False

# A sample solution
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
print(sudoku(puzzle))
