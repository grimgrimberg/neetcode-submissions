import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key - (r/3,c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #if empty continue
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares [(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True

        # list_nums = list(range(1,10,1))
        # print(list_nums)
        # seen = set()
        # #row checker
        # for i in range(len(board)):
        #     for j in range(len(board)):
        #         duplicates_row = [x for x in board[i] if x in seen or seen.add(x)]
        #         if 

        # return 0