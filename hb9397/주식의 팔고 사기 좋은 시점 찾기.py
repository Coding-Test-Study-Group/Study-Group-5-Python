# 문제 요약
# 주식의 가격 정보가 1차원 배열 prices 에 담겨서 주어지는 이를 최대 이득이 되게 사고 팔려고 할 때 최대 이득은 얼마인가?
# 이 때 주식의 가격은  0 ~ 10000 을 가지고 시간 복잡도는 O(n^2) 작아야 한다.
# ex1 : prices = [7, 1, 5, 3, 6, 4] -> result = 5
# ex2 : prices = [7, 6, 4, 3, 1] -> result = 0
""" import time
def solution(price):
    answer = 0

    minimum = min(price)
    price = price[price.index(min(price)):]
    answer = max(price) - minimum

    return answer """

# 반례 -> [7, 6, 4, 2, 5, 1] 이 prices로 주어지면 바로 최소값을 찾기 때문에 2에 사고 5에 파는 것이 최대 이득 3 을 갖을 수 있지만
#         처음 부터 최소값을 찾아서 그 이후로 슬라이싱 하면 반환하는 최대 이득은 0이 된다.

# 주식의 가격이 담긴 배열에 차례대로 접근 --- 1
# 접근한 가격과 현재 기억하고 있는 주식의 최소 가격을 비교해서 더 작은 값을 주식의 최소가격으로 설정 --- 2
# 현재 접근한 가격에서 최대로 얻을 수 있는 이익은 현재 기억하고 있는 최대 이익과 
# [현재 접근한 주식의 가격 - 현재 기억하고 있는 주식의 최소 가격] 을 비교 해서 더 큰 값이 된다. --- 3
# 최대 이익의 초기값은 모든 가격을 위 처럼 비교 했을 때 주식을 구매한 시점에 바로 팔아야 하는 경우가 가장 큰 이익을 가져올 때의 0으로 설정 --- 4
# 주식의 최소 가격의 초기값은 주식이 가질 수 있는 최대 가격인 10000 으로 설정해서 입력값의 모든 경우에 해당 될 수 있게 한다. --- 5
def solution(prices):
    max_profit = 0 # 4
    min_price = 10000 # 5

    for current_price in prices: # 1
        min_price = min(min_price, current_price) # 2
        max_profit = max(max_profit, current_price - min_price) #3
       
    return max_profit
