class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def backtrack(r, c, i):
            # matched the whole word
            if i == len(word):
                return True

            # outside the board
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # already used this cell in the current path
            if (r, c) in seen:
                return False

            # current cell does not match current letter
            if board[r][c] != word[i]:
                return False

            # choose this cell
            seen.add((r, c))

            # try to match the next letter in all 4 directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if backtrack(nr, nc, i + 1):
                    seen.remove((r, c))
                    return True

            # un-choose this cell
            seen.remove((r, c))
            return False

        # try every cell as a possible starting point
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
        # dirct = [(1,0),(-1,0),(0,1),(0,-1)] #down, up, right,left
        # row = len(board)
        # col = len(board[0])
        # seen = set()
        # def backtrack(r, c, i):
        #     if not word:
        #         return True
        #     # seen.add((r,c))
        #     for dir in dirct:
        #         nr,nc = r+dir[0],c+dir[1]
        #         if nr>=row or nr <0 or nc <0 or nr>=col: #if outside
        #             continue
        #         else:
        #             seen.add((nr,nc))
        #         if word[0] == board[nr][nc] and (nr,nc) not in seen : #if start of word in valid box
        #             return self.backtrack(board,word[1:],nr,nc)
        # return False
        # for r in range(row):
        #     for c in range(col):
        #         backtrack(r,c,0)
        

