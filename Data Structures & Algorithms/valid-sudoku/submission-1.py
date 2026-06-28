class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for fila in board: #filas
            vistos=set()
            for celda in fila:
                if celda==".":
                    continue
                if celda in vistos:
                    return False
                else:
                    vistos.add(celda)
        #columnas
        for columna in range(9):
            vistos=set()
            for elemento in range(9):
                celda=board[elemento][columna]
                if celda ==".":
                    continue
                if celda in vistos:
                    return False
                else:
                    vistos.add(celda)
        #cajitas

        for fila_inicio in range(0,9,3):
            for col_inicio in range(0,9,3):
                vistos=set()
                for fila in range(fila_inicio, fila_inicio+3):
                    for col in range(col_inicio, col_inicio+3):
                        if board[fila][col]==".":
                            continue
                        if board[fila][col] in vistos:
                            return False
                        if board[fila][col] not in vistos:
                            vistos.add(board[fila][col])
                        
        return True