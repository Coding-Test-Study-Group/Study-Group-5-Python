import time
def solution(price):
    answer = 0

    minimum = min(price)
    price = price[price.index(min(price)):]
    answer = max(price) - minimum

    return answer

start = time.time()
print(solution([7, 1, 5, 3, 6, 4]))
end = time.time()
print(end - start)
print("\n")

start = time.time()
print(solution([7, 6, 4, 3, 1]))
end = time.time()
print(end - start)
print("\n")

start = time.time()
print(solution([1, 2, 4, 7, 8, 100, 3, 1000]))
end = time.time()
print(end - start)
