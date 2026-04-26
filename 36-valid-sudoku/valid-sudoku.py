class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                keys = [
                    ("row", r, num),
                    ("col", c, num),
                    ("box", r // 3, c // 3, num)
                ]

                for k in keys:
                    if k in seen:
                        return False
                    seen.add(k)
        return True
