from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        def is_valid_block(start_row, start_col):
            seen = set()
            for i in range(3):
                for j in range(3):
                    val = board[start_row + i][start_col + j]
                    if val != ".":
                        if val in seen:
                            return False
                        seen.add(val)
            return True

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not is_valid_block(r, c):
                    return False

        return True