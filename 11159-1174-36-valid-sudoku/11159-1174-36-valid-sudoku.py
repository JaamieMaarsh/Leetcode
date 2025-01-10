class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        column_map = defaultdict(set)
        subbox_map = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == '.':
                    continue
                
                value = board[row][col]

                if value in row_map[row] or value in column_map[col] or value in subbox_map[row//3, col//3]:
                    return False
                
                row_map[row].add(value)
                column_map[col].add(value)
                subbox_map[row//3, col//3].add(value)
        
        return True