# Generate a list of solutions on a board with rows and columns.
# A solution is given by a list of column positions, indicated by 
# row number.
# Indices begin with zero.
def queenproblem(rows, columns):
    if rows <= 0:
        return [[]] # no queen to place; empty board is solution
    else:
        return one_more_queen(rows - 1, columns, queenproblem(rows - 1, columns))
 
# Try all columns in which, for a given partial solution,
# a queen can be placed in "new_row".
# If no conflict with the partial solution occurs,
# a new solution for the board extended by one row
# is found.
def one_more_queen(new_row, columns, previous_solutions):
    new_solutions = []
    for solution in previous_solutions:
        # Attempt to insert a queen in each column of new_row.
        for new_column in range(columns):
            # print('trying: %s in row %s' % (new_column, new_row))
            if no_conflict(new_row, new_column, solution):
                # No conflicts, so this attempt is a solution.
                new_solutions.append(solution + [new_column])
    return new_solutions
 
# Can a queen be placed at position "new_column"/"new_row"
# without attacking the queens already present?
def no_conflict(new_row, new_column, solution):
    # Make sure that the new queen does not occupy a row or diagonal 
    # with any of the existing queens.
    for row in range(new_row):
        # print(solution, row, new_column, new_row)
        if (solution[row]       == new_column              or  # Same column.
            solution[row] + row == new_column + new_row or  # Same diagonal.
            solution[row] - row == new_column - new_row):    # Same diagonal.
                return False
    return True

for solution in queenproblem(8, 8):
    print(solution)


