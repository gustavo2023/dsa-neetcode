class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board)):
                value = board[row][col]

                if value == ".":
                    continue

                box_index = (row // 3) * 3 + (col // 3)

                if value in rows[row] or value in cols[col] or value in boxes[box_index]:
                    return False
                
                rows[row].add(value)
                cols[col].add(value)
                boxes[box_index].add(value)

        return True

                