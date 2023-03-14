def solution(gems):
    N = len(gems) # 배열 길이 자주 쓰니까 변수 선언해두기~
    types = len(set(gems)) # 보석이 총 몇 종류인지 알아두기
    dic = {gems[0]: 1} # 보석이 종류 별로 몇 개인지 체크하기 위한 dic(map)
    answer = [0, N - 1] # 정답 배열에 처음과 끝을 넣어 놓기
    
    # 투 포인터
    l, r = 0, 0
    while l < N and r < N:
        # dic에 보석 종류가 다 있는 경우
        if len(dic) == types:
            # l과 r 사이의 거리를 확인하여 더 짧을 때의 값을 가지고 있기
            if r - l < answer[1] - answer[0]:
                answer = [l, r]
            # l과 r 사이의 거리를 확인했는데 가지고 있는 값보다 더 길다면? 정답이 아님! 따라서 l을 조정(l을 앞으로 한칸 보내기)해야 함
            # l을 앞으로 한 칸 보내기 전에 dic에서 그 한 칸에 대한 종류를 찾아서 개수 1개를 빼준다.
            # 뺐는데 0이면 아예 dic에서 없앤다.
            dic[gems[l]] -= 1
            if dic[gems[l]] == 0:
                del dic[gems[l]]
            # l을 앞으로 한 칸 보낸다.
            l += 1
        # dic에 보석 종류가 다 있는 게 아니면? r을 앞으로 한 칸 옮겨서 종류를 채워준다.
        else:
            r += 1
            # r이 끝까지 갔다면? 나와~
            if r == N:
                break
            # r이 끝까지 간 게 아니면 앞으로 1칸 보내도 된다.
            # r을 앞으로 한 칸 보내기 전에 dic에서 그 한 칸에 대한 종류를 찾아서 개수 1개를 더해준다.
            # 종류가 아예 없다면 새로 만들고, 이미 있다면 +1을 한다.
            dic[gems[r]] = dic.get(gems[r], 0) + 1
    
    # 인덱스가 0부터 시작했으므로 +1을 해준다.
    return [answer[0] + 1, answer[1] + 1]