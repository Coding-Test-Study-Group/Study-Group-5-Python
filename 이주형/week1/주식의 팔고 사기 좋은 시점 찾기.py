def solution(s):
    h = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if h < s[j] - s[i]:
                h = s[j] - s[i]
    print(h)

solution([6,2,4,1])