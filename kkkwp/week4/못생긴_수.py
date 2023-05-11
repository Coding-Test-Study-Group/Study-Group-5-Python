import sys
input = sys.stdin.readline

n = int(input())

ugly = [0] * n # 못생긴 수들의 모임~
ugly[0] = 1 # 첫번째 못생긴 수는 1

i2, i3, i5 = 0, 0, 0 # 인덱스
n2, n3, n5 = 2, 3, 5 # 곱할 수

for i in range(1, n):
    ugly[i] = min(n2, n3, n5)
    if ugly[i] == n2:
        i2 += 1
        n2 = ugly[i2] * 2
    if ugly[i] == n3:
        i3 += 1
        n3 = ugly[i3] * 3
    if ugly[i] == n5:
        i5 += 1
        n5 = ugly[i5] * 5

print(ugly[n - 1])