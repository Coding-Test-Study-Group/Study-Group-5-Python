import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0    
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] != -1:
                continue
            q.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

n, m = map(int, input().split())
x, y = map(int, input().split())

enemy = []
for _ in range(m):
    a, b = map(int, input().split())
    enemy.append((a, b))

board = [[-1 for _ in range(n)] for __ in range(n)]

bfs(x - 1, y - 1)

for x, y in enemy:
    print(board[x - 1][y - 1], end=' ')