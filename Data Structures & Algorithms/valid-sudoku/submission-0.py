class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardValues = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                value = board[row][col]
                if value == '.':
                    continue
                rowKey = f'row_{row}'
                colKey = f'col_{col}'
                boxIdx = (row // 3) * 3 + (col // 3)
                boxKey = f'box_{boxIdx}'

                if value in boardValues[rowKey] or value in boardValues[colKey] or value in boardValues[boxKey]:
                    return False

                boardValues[rowKey].add(value)
                boardValues[colKey].add(value)
                boardValues[boxKey].add(value)

        return True


