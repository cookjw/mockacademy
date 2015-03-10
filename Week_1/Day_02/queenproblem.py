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
        # Versuche, eine Dame in jeder Spalte von neue_reihe einzufügen.
        for new_column in range(columns):
            # print('trying: %s in row %s' % (new_column, new_row))
            if no_conflict(new_row, new_column, solution):
                # No conflicts, so this attempt is a solution.
                new_solutions.append(solution + [new_solutions])
    return new_solutions
 
# Can a queen be placed at position "new_column"/"new_row"
# without attacking the queens already present?
def no_conflict(new_row, new_column, solution):
    # Stelle sicher, dass die neue Dame mit keiner der existierenden
    # Damen auf einer Spalte oder Diagonalen steht.
    for row in range(new_row):
        if (solution[row]         == new_column              or  # Gleiche Spalte
            solution[row] + row == new_column + new_row or  # Gleiche Diagonale
            solution[row] - row == new_column - new_row):    # Gleiche Diagonale
                return False
    return True
 
for solution in queenproblem(8, 8):
    print(solution)

# # Erzeuge eine Liste von Lösung auf einem Brett mit Reihen und Spalten.
# # Eine Lösung wird durch eine Liste der Spaltenpositionen,
# # indiziert durch die Reihennummer, angegeben.
# # Die Indizes beginnen mit Null.
# def damenproblem(reihen, spalten):
#     if reihen <= 0:
#         return [[]] # keine Dame zu setzen; leeres Brett ist Lösung
#     else:
#         return eine_dame_dazu(reihen - 1, spalten, damenproblem(reihen - 1, spalten))
 
# # Probiere alle Spalten, in denen für eine gegebene Teillösung
# # eine Dame in "neue_reihe" gestellt werden kann.
# # Wenn kein Konflikt mit der Teillösung auftritt,
# # ist eine neue Lösung des um eine Reihe erweiterten
# # Bretts gefunden.
# def eine_dame_dazu(neue_reihe, spalten, vorherige_loesungen):
#     neue_loesungen = []
#     for loesung in vorherige_loesungen:
#         # Versuche, eine Dame in jeder Spalte von neue_reihe einzufügen.
#         for neue_spalte in range(spalten):
#             # print('Versuch: %s in Reihe %s' % (neue_spalte, neue_reihe))
#             if kein_konflikt(neue_reihe, neue_spalte, loesung):
#                 # Kein Konflikte, also ist dieser Versuch eine Lösung.
#                 neue_loesungen.append(loesung + [neue_spalte])
#     return neue_loesungen
 
# # Kann eine Dame an die Position "neue_spalte"/"neue_reihe" gestellt werden,
# # ohne dass sie eine der schon stehenden Damen schlagen kann?
# def kein_konflikt(neue_reihe, neue_spalte, loesung):
#     # Stelle sicher, dass die neue Dame mit keiner der existierenden
#     # Damen auf einer Spalte oder Diagonalen steht.
#     for reihe in range(neue_reihe):
#         if (loesung[reihe]         == neue_spalte              or  # Gleiche Spalte
#             loesung[reihe] + reihe == neue_spalte + neue_reihe or  # Gleiche Diagonale
#             loesung[reihe] - reihe == neue_spalte - neue_reihe):    # Gleiche Diagonale
#                 return False
#     return True
 
# for loesung in damenproblem(8, 8):
#     print(loesung)