from collections import deque

def solution(n):
    cards = deque([i for i in range(1, n + 1)])
    while len(cards) > 1:
        cards.popleft()
        top = cards.popleft()
        cards.append(top)        
    return cards[0]