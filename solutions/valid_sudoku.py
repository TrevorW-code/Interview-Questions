class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        active_board = []

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    # create three tuples
                    # 1. Row Check
                    # 2. Column Check
                    # 3. Sub Box Check (floor division creates sub boxes)
                    active_board += [(i,element), (element,j), (i // 3, j // 3, element)]

        return len(active_board) == len(set(active_board)) # checks if there are duplicates. If there are, return False, else True.