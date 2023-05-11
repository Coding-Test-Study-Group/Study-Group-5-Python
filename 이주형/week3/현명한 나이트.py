from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    board[x][y] = 0

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 8가지 방향으로 위치 확인
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if board[nx][ny] != -1:
                continue
            
            queue.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

N, M = map(int, input().split())
x, y = map(int, input().split())

graph = []
for i in range(M):
    a, b = map(int, input().split())
    graph.append((a, b))

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

board = [[-1 for i in range(N)] for i in range(N)]

bfs(x - 1, y - 1)

for x, y in graph:
    print(board[x - 1][y - 1], end=' ')