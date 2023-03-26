def solution(arr):
    n = len(arr) // 2 + 1 # 숫자 개수
    max_dp = [[-float('inf') for _ in range(n)] for _ in range(n)]
    min_dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        max_dp[i][i] = int(arr[i*2])
        min_dp[i][i] = int(arr[i*2])

    for step in range(1, n): # i와 j의 간격
        for i in range(n - step): # i부터 j까지의 연산을 수행
            j = i + step
            for k in range(i, j): # i부터 j까지 돌면서, 괄호를 한칸씩 늘리고 줄인다.
                if arr[k*2+1] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j]) # + 인 경우, 최댓값은 최댓값 + 최댓값
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j]) # + 인 경우, 최솟값은 최솟값 + 최솟값
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j]) # - 인 경우, 최댓값은 최댓값 - 최솟값
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j]) # - 인 경우, 최솟값은 최솟값 - 최댓값

    return max_dp[0][n-1]