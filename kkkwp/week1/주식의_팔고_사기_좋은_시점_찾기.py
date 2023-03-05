def solution(prices):
    answer = 0
    min_val = float('inf')
    for price in prices:
        min_val = min(min_val, price)
        answer = max(answer, price - min_val)
    return answer