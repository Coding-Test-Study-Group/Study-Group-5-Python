import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] != 1:
                continue
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))
    return board[n - 1][m - 1]

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

print(bfs(0, 0))