import collections

class Solution:
    def solve1(self, board: List[List[str]]) -> None:
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()
        m, n = len(board), len(board[0])
        
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i,0))
            if board[i][n-1] == 'O':
                q.append((i, n-1))
        
        for j in range(n):
            if board[0][j] == 'O':
                q.append((0,j))
            if board[m-1][j] == 'O':
                q.append((m-1,j))
                
        def check_bound(x,y):
            return (0 <= x < m) and (0 <= y < n)
        
        while q:
            i, j = q.popleft()
            board[i][j] = 'Z'
            
            for i_x, j_y  in directions:
                xx = i + i_x
                yy = j + j_y
                
                if not check_bound(xx,yy):
                    continue
                if board[xx][yy] != 'O':
                    continue
                
                q.append((xx,yy))
                board[xx][yy] = 'Z'
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                    
                    
                    
    def solve(self, board: List[List[str]]) -> None:
        if not any(board): return
        
        m, n = len(board), len(board[0])
        answer = []
        
        for i in range(m):
            answer.append((i,0))
            answer.append((i,n-1))
            
        for j in range(n):
            answer.append((0,j))
            answer.append((m-1,j))
            
        while answer:
            i, j = answer.pop()
            if 0 <= i < m and 0<= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                answer += (i+1, j), (i-1, j), (i, j+1), (i, j-1)
                
        board[:] = [['XO'[col == 'S'] for col in row] for row in board]
        
        
                    
                    
                
                
        
        