from collections import deque

def solution(s):
    queue = deque()

    for i in range(1, s+1):
        queue.append(i)
    
    while len(queue)>1:
        queue.popleft()
        queue.append(queue.popleft())

    print(queue[0])

solution(6)