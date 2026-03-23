class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n=len(board)
        m=len(board[0])

        def dfs(i,j,word_i):
            if(len(word)<=word_i):
                return True
            if((0 <= i < n) and (0 <= j <m) and board[i][j]==word[word_i] and board[i][j]):
                temp = board[i][j]
                board[i][j] = ''
                a=dfs(i+1,j,word_i+1)
                b=dfs(i,j+1,word_i+1)
                c=dfs(i-1,j,word_i+1)
                d=dfs(i,j-1,word_i+1)
                board[i][j] = temp
                return a or b or c or d
            return False



        for i in range(n):
            for j in range(m):
                if(word[0]==board[i][j]):
                    boolean= dfs(i,j,0)
                    if(boolean==True):
                        return True
        return False