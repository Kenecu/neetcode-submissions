class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                box_sec = (i//3,j//3)
                if val in row[i] or val in column[j] or val in boxes[box_sec]:
                    return False
                row[i].add(val)
                column[j].add(val)
                boxes[box_sec].add(val)
        return True
                