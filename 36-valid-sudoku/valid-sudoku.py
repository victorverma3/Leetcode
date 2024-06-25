class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            row = set()
            col = set()
            for j in range(len(board)):
                if board[i][j] in row:
                    return False
                elif board[i][j] != ".":
                    row.add(board[i][j])
                if board[j][i] in col:
                    return False
                elif board[j][i] != ".":
                    col.add(board[j][i])
        print("rows and columns ok")

        centers = [1, 4, 7]
        for i in centers:
            for j in centers:
                values = set()
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if board[k][l] in values:
                            return False
                        elif board[k][l] != ".":
                            values.add(board[k][l])
        return True