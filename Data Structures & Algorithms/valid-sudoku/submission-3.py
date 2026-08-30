class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(len(board)):
            for c in range(len(board)):
                value = board[r][c]

                if value == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if value in rows[r] or value in cols[c] or value in boxes[box_index]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)
        
        return True  

                