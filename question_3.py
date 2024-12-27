def solve_n_queens(n):
    def is_safe(row, col):
        return not (columns[col] or main_diag[row - col] or anti_diag[row + col])

    def place_queen(row, col):
        columns[col] = main_diag[row - col] = anti_diag[row + col] = True
        queens[row] = col

    def remove_queen(row, col):
        columns[col] = main_diag[row - col] = anti_diag[row + col] = False
        queens[row] = -1

    def backtrack(row):
        if row == n:
            solutions.append(queens[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                place_queen(row, col)
                backtrack(row + 1)
                remove_queen(row, col)

    solutions = []
    queens = [-1] * n  
    columns = [False] * n
    main_diag = [False] * (2 * n - 1) 
    anti_diag = [False] * (2 * n - 1) 

    backtrack(0)
    return solutions


# Example
n=4
print(solve_n_queens(n))
