import time
def solution1(N):
    answer = 0
    temp = [i for i in range(N, 0, -1)]

    while len(temp) != 2:
        temp.pop()
        temp.insert(0, temp.pop())

    answer = temp[0]
    return answer

from collections import deque
def solution2(N):
    answer = 0
    temp = deque(i for i in range(1, N+1))

    while len(temp) != 1:
        temp.popleft()
        temp.append(temp.popleft())

    answer = temp[0]
    return answer



start = time.time()
print(solution1(4))
end = time.time()
print(end - start)
print("\n")

start = time.time()
print(solution1(6))
end = time.time()
print(end - start)
print("\n")

start = time.time()
print(solution1(1000))
end = time.time()
print(end - start)
print("\n")

start = time.time()
print(solution2(4))
end = time.time()
print(end - start)
print("\n")

start = time.time()
print(solution2(6))
end = time.time()
print(end - start)
print("\n")

start = time.time()
print(solution2(1000))
end = time.time()
print(end - start)
print("\n")