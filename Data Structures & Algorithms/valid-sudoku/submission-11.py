class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == ".":
                    continue
                section = (i//3, j//3)
                if current in rows[i] or current in cols[j] or current in boxes[section]:
                    return False
                rows[i].add(current)
                cols[j].add(current)
                boxes[section].add(current)
        return True