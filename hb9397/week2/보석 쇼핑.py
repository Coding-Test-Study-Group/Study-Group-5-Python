#https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    answer = [0, 0]

    # gems[lp ~ rp]까지 탐색했을 때 보석의 개수를 저장
    curGems = {} 

    # gems 에 주어진 보석의 종류 개수
    gemsKind = len(set(gems))

    # 현재 탐색한 최소 gems[lp ~ rp] 에 대한 진열대의 길이 초기값은 진열대의 최대 길이 (1 부터 시작)
    curSection = len(gems) + 1
    
    lp = 0
    rp = 0

    while rp < len(gems) and lp < len(gems):

        if gems[rp] not in curGems:
            curGems[gems[rp]] = 1
            rp += 1
        elif gems[rp] in curGems:
            curGems[gems[rp]] += 1
            rp += 1

        if len(curGems) == gemsKind:
            while lp <= rp:
                if curGems[gems[lp]] > 1:
                    curGems[gems[lp]] -= 1
                    lp += 1
                elif curSection > rp - lp:
                    answer[0] = lp + 1
                    curSection = rp - lp
                    break
                else:
                    break

    return answer

# 코드 해석
def solution(gems):
    answer = [0, 0]

    # gems[lp ~ rp]까지 탐색했을 때 보석의 개수를 저장
    curGems = {} 

    # gems 에 주어진 보석의 종류 개수
    gemsKind = len(set(gems))

    # 현재 탐색한 최소 gems[lp ~ rp] 에 대한 진열대의 길이 초기값은 진열대의 최대 길이 (1 부터 시작)
    curSection = len(gems) + 1
    
    lp = 0
    rp = 0
    
    # lp와 rp 는 현재 탐색중인 gems 의 index 로 gems 의 길이보다 작은 만큼만 탐색
    while rp < len(gems) and lp < len(gems):

        # 현재 오른쪽 포인터가 가리키는 gems의 보석이 현재까지 탐색한 curGems 에 있지 않다면
        # 새로운 보석을 발견 했기 때문에 보석의 종류를 key로 주어 보석 종류가 중복되지 않게 하고
        # 처음 보는 보석으로 count 를 value로 갖게 하기 위해 1로 준다.
        # 이후 gems의 다음 rp 에 대한 탐색을 위해 1 증가
        if gems[rp] not in curGems:
            curGems[gems[rp]] = 1
            rp += 1

        # 현재 오른쪽 포인터가 가리키는 gems의 보석이 새로운 보석이 아닌 경우에 해당 보석 key의 value 에 1을 더해준다.
        # 이후 gems의 다음 rp 에 대한 탐색을 위해 1 증가
        elif gems[rp] in curGems:
            curGems[gems[rp]] += 1
            rp += 1
            
        # 탐색하던 도중 현재 탐색한 보석의 종류개수가 gems에 주어진 모든 종류의 보석을 탐색했을 때, rp의 증가를 멈추고
        # lp의 길이가 rp와 같을 때까지만 반복해서 lp 가 가리키는 gems의 index를 증가시키기 위해서 lp를 증가시키면서
        # 모든 보석의 종류를 포함해서 탐색하는 최소 거리에 대한 유효성 검사를 진행한다.
        if len(curGems) == gemsKind:
            while lp <= rp:

                # 현재 탐색한 보석의 종류와 개수를 저장한 curGems에서 lp가 가리키는 gems 내의 보석의 종류 개수가 1개 이상이라면 
                # 현재 lp가 가리키는 gems는 굳이 포함 시키지 않아도 뒤에 존재하므로 현재 curGems 에서
                # 현재 lp가 가리키는 gems의 보석 종류 개수를 1 감소 시킨다. (탐색 범위에서 제거할 것이기 때문에)
                # 이후 탐색 범위를 좁히기 위해서 lp를 1 증가시킨다.
                if curGems[gems[lp]] > 1:
                    curGems[gems[lp]] -= 1
                    lp += 1
                
                # 또한 lp를 증가시키므로 인해서 현재 탐색한 범위는 줄어 들게 되는데 이 범위 내에 
                # gems 의 모든 종류의 보석이 있는 것이 보장 되므로 현재 기억하고 있는 탐색 범위보다
                # 현재 rp의 증가를 멈추고 lp를 증가시켜서 축소된 탐색 범위가 더 작다면 그 범위가 가장 최소의 거리로 진열대를 탐색해서
                # 모든 종류의 보석을 쇼핑할 수 있는 경우가 된다.
                elif curSection > rp - lp:

                    # 진열대의 시작 번호는 1부터 시작해서 lp 는 1을 더해야 하지만
                    answer[0] = lp + 1

                    # rp 는 새로운 보석이든 아니든 무조건 gems 에서 rp가 가리키는 다음 index를 탐색하기 위해서 +1 이 된 상태로 
                    # 해당 while문으로 넘어오기 때문에 +1 을 하지 않아도 진열대의 번호와 같다 
                    # (길이의 값이 최소인지 판별하는데는 문제가 없다.)
                    answer[1] = rp

                    # 현재 최소로 탐색해서 모든 종류의 보석을 구매할 수 있는 범위 갱신
                    curSection = rp - lp

                    # 또한 현재 탐색한 범위에서 모든 gems의 종류가 나왔으니 break 로 현재 유효성 검사를 그만 진행하고 
                    # 현재 최소 범위를 기억하고
                    # 다시 lp를 증가 시킨 더 좁아진 범위에 gems 의 모든 종류의 보석이 들어있는지 판별하기 위해서 while문 탈출
                    break
                    
                # lp~rp가 가리키는 범위가 현재 기억하고 있는 최소 범위 보다 크거나
                # 현재 lp가 gems에서 가리키는 보석이 처음 보는 보석인지 판별해서 while 문 탈출(종료)
                else:
                    break

    return answer