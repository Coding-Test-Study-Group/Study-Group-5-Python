# https://www.acmicpc.net/problem/2178
from collections import deque

N, M = map(int, input().split())

miro = [list(map(int, input())) for _ in range(N)]

go = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(y, x):
    temp = deque()
    temp.append((y, x))

    while temp:
        cY, cX = temp.popleft()
        for goY, goX in go:
            Y, X = cY + goY, cX + goX

            if Y == 0 and X == 0:
                continue

            if (0 <= Y < N) and (0 <= X < M) and miro[Y][X] == 1:
                temp.append((Y, X))
                miro[Y][X] += miro[cY][cX]

# 풀이 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 미로의 최초 좌표값(미로 탐색 시작값)
bfs(0, 0)
print(miro[N-1][M-1])

from collections import deque
# N은 도달 해야하는 좌표의 y값, M은 도달 해야하는 좌표의 X값
# 한 줄에 입력된 N M을 , 로 분리해서 N, M에 할당 
N, M = map(int, input().split())

# 미로는 입력값의 첫번째 줄을 제외한 미로의 N줄만큼 생긴다.
# miro 의 index 에는 이동 가능 / 불가능을 가리키는 1과 0을 초기값으로 가지게 하고 이동 가능한 miro 의 좌표에는 현재 좌표까지 이동한 만큼 1들의 값을 더한 값이 들어가게된다.
# 입력 받을 때, 101101 과 같이 한 줄에 붙어서 입력되는 정수를 1, 0, 1, 1, 0, 1 과 같이 나눠서 하나의 list로 담기 위한 작업
miro = [list(map(int, input())) for _ in range(N)]

# 미로는 인접한 좌표로만 이동할 수 있다 -> 상하좌우
# 위의 좌표가 이동 가능한 값을 상대적으로 나타낸다.
# 이 때 좌표가 이동 가능한 값을 상대적으로 나타내는 해당 배열도 순회하여 현재 좌표에 연산하기 때문에
# 좌표 탐색 시작점이 이동 가능한 이동 값을 먼저 주어야 한다. (이 문제에서는 미로의 탐색점은 1, 1 즉 0, 0 부터 탐색하기 때문에 갈 수 최초로 이동할 수 있는값은
# 밑으로 이동하는 것과 우측으로 이동하는 것이다.
go = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# bfs 를 이용해서 현재 좌표를 입력 받아서 temp라는 deque 에 삽입한 뒤, 
# 현재 좌표에서 go의 조건으로 이동 가능한 좌표(미로에 존재하는 좌표) 조건과 0과 1로  이동 가능 여부 따지는 조건을 모두 만족해야 이동이 가능한 좌표로 취급하고
# 갈 수 있는 좌표에 대해서는 기록, 기록된 좌표로 이동하기 위해서 현재까지 이동한 횟수를 이동한 좌표의 값으로 갖게 한다.
# 이 때 문제의 조건에서 미로의 시작부터 1칸 으로 count 하기 때문에 시작값부터 가지고 있는 1의 값(현재 좌표까지의 이동횟수의 초기값)을 더해준다.
# 이렇게 되면 미로의 마지막인 탈출구 N, M 까지 도달하기 위해서 이동한 횟수를 miro[N-1][M-1]에 기록할 수 있다.
def bfs(y, x):
    temp = deque()
    temp.append((y, x))

    while temp:
        cY, cX = temp.popleft()
        for goY, goX in go:
            Y, X = cY + goY, cX + goX

            if Y == 0 and X == 0:
                continue

            if (0 <= Y < N) and (0 <= X < M) and miro[Y][X] == 1:
                temp.append((Y, X))
                miro[Y][X] += miro[cY][cX]

# 미로의 최초 좌표값(미로 탐색 시작값)
bfs(0, 0)
print(miro[N-1][M-1])