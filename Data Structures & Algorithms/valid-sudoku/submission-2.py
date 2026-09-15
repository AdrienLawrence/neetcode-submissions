class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []
        columns = []
        boxes = []
        for i in range(0, 9):
            rows.append(set())

        for j in range(0, 9):
            columns.append(set())
        
        for k in range(0, 9):
            boxes.append(set())

        for i in range(0, len(board)):

            for j in range(0, len(board[0])):

                if board[i][j] == ".":
                    continue

                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                

                if board[i][j] in columns[j]:
                    return False
                else:
                    columns[j].add(board[i][j])
                
                if board[i][j] in boxes[(i//3) + 3*(j//3)]:
                    return False
                else:
                    boxes[(i//3) + 3*(j//3)].add(board[i][j])

        return True






