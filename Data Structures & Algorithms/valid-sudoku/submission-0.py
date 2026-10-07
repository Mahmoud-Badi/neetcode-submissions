class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)  # digits seen so far in each row
        cols = defaultdict(set)  # digits seen so far in each column
        boxes = defaultdict(set) # digits seen so far in each 3x3 box

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":  # empty cell, nothing to check
                    continue

                # (r // 3, c // 3) labels the box: 0 to 2 down, 0 to 2 across
                box = (r // 3, c // 3)

                # seen this digit before in the same row, column, or box? invalid
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                # first time seeing it in all three groups, so record it
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True

        # Time = O(81), Space = O(81), both constant since the board is always 9x9