from collections import deque

# 너비 우선 탐색
def bfs(x, y):
  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      
      # 벽이 아니고 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[N-1][M-1]

N, M = map(int, input().split())

graph = []

for i in range(N):
  graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

print(bfs(0, 0))