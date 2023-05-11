# # # DFS알고리즘을 이용하여 하나하나씩 탐색하여 없으면 다음 단계로 넘어간다.
# def solution(my_night, enemy_night):
#     X = my_night[0]
#     Y = my_night[1]
#     answer = []
#     switch_night=[[X-2,Y-1], [X-2,Y+1], [X-1,Y-2], [X-1,Y+2], [X+1,Y-2], [X+1,Y+2], [X+2,Y-1], [X+2,Y+1]] # X,Y값들을 계산하여 이동할수 있는 위치를 찾는다.
#     for i in enemy_night: # 상대 말 위치를 하나씩 대입하여 이동할 위치에 있는지 비교
#         cnt = 0
#         print(cnt)
#         print(i)
#         if i in switch_night: #이동 위치에 상대방 위치가 있는지 탐색
#             cnt += 1 # 카운트를 해주나, 초기값설정을 어느부분에 해주어야하는지 어떻게 해주어야하는지 탐색이 필요
#             answer.append(cnt)
#             print(cnt)
#             print(answer)
#         elif i not in switch_night: # 이동할 위치에 적 위치가 없을시 재귀함수를 사용하고자 한다...
#             cnt += 1
#             solution(i,i)    
#     return answer

# a = [2, 4]
# b = [[3,2], [3,5], [4,5]]
# print(solution(a, b))

# #---------------------------


# bfs를 구현하기 위한 deque 로드
from collections import deque
# 빠른 입력을 위한 stdin 로드 -> 반복문을 여러번 받을때 시간초과가 발생할수 있지만 stdin을 사용해 방지
from sys import stdin
input = stdin.readline

# 거리의 최대값 상수 설정
MAX_DISTANCE = int(1e5)
# n은 체스판 크기, m은 상대 말 갯수
n, m = map(int, input().split())

# 현재 나이트 위치
x, y = map(int, input().split())
x, y = x-1, y-1 
# 적 말들 위치 저장
enemy = [] 

for _ in range(m):
    dx, dy = map(int, input().split())
    enemy.append((dx - 1, dy - 1)) 


# 나이트 이동 범위 설정 
#(X-2,Y-1), (X-2,Y+1), (X-1,Y-2), (X-1,Y+2), (X+1,Y-2), (X+1,Y+2), (X+2,Y-1), (X+2,Y+1)
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

# 방문 처리 용  초기값 False로 설정
visited = [[False for _ in range(n)] for __ in range(n)]


# n x n의 보드판 생성 및 도달 할 수 있는 거리 생성
board = [[MAX_DISTANCE for _ in range(n)] for __ in range(n)]

# bfs를 통해 움직일 수 있으면 거리 추가
queue = deque([(x, y)])
# 나이트의 초기값은 움직이지 않았으므로 0
board[y][x] = 0
while queue:
    c_x, c_y = queue.popleft() 
    if visited[c_y][c_x]: # 삭제된 값을 visited에 넣어 확인한다.
        continue   #해당 위치가 방문인 경우 continue를 실행
    visited[c_y][c_x] = True # True로 변경한다.
    for i in range(8): 
        mx, my = c_x + dx[i], c_y + dy[i]  
        # 현재 나이트가 이동할 위치가 체스판 범위내에 있는지 확인하는 부분
        if 0 <= mx < n and 0 <= my < n: 
            # 현재 나이트가 이전에 방문했던 위치에서 이동거리에 1을 더한값과
            # 현재 위치의 거리중 더 작은 값을 저장하는 부분이다.
            # 이전 위치에서 현재 위치로 이동하는 거리가 더 짧은 경우 이전에 저장된 최단거리 값을 갱신한다.
            board[my][mx] = min(board[my][mx], board[c_y][c_x] + 1)
            # 방문하지 않은 부분을 queue에 추가하는 부분
            queue.append((mx, my))
print(board)
for ex, ey in enemy:
    print(board[ey][ex], end=" ")