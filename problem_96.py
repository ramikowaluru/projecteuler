import re


def print_grid(sudoku_matrix):
    for i in range(9):
        for j in range(9):
            print(sudoku_matrix[i][j], end=' ')
        print('n')


def retrieve_unsolved_location(sudoku_matrix, l):
    for row in range(9):
        for col in range(9):
            if sudoku_matrix[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


def repeated_in_row(sudoku_matrix, row, num):
    for i in range(9):
        if sudoku_matrix[row][i] == num:
            return True
    return False


def reapeated_in_column(sudoku_matrix, col, num):
    for i in range(9):
        if sudoku_matrix[i][col] == num:
            return True
    return False


def used_in_box(sudoku_matrix, row, col, num):
    for i in range(3):
        for j in range(3):
            if sudoku_matrix[i + row][j + col] == num:
                return True
    return False


def fixing_value_at_unsolved_location(sudoku_matrix, row, col, num):
    return not repeated_in_row(sudoku_matrix, row, num) and not reapeated_in_column(sudoku_matrix, col, num) and not used_in_box(sudoku_matrix, row - row % 3,
                                                                                                 col - col % 3, num)


def solve_sudoku(sudoku_matrix):
    l = [0, 0]

    if not retrieve_unsolved_location(sudoku_matrix, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if fixing_value_at_unsolved_location(sudoku_matrix, row, col, num):
            sudoku_matrix[row][col] = num
            if solve_sudoku(sudoku_matrix):
                return True
            sudoku_matrix[row][col] = 0
    return False


if __name__ == '__main__':
    with open('./data/p096_sudoku.txt', 'r') as f:
        sudokus = f.readlines()

    sudokus = re.compile("Grid [0-9][0-9]").split(''.join(sudokus))[1:]

    s = 0
    for i in sudokus:
        grid = list()
        for j in i.split('\n')[1:-1]:
            grid.append((list(map(int, list(j)))))
        if solve_sudoku(grid):
            s += int(''.join((map(str, grid[0][:3]))))
            print(grid[0][:3])
        else:
            print("No Solution")
        print(s)