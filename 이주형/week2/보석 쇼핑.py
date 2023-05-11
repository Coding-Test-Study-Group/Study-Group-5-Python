def solution(gems):
    answer = [0, len(gems) - 1]
    kind = len(set(gems))  # 보석 종류의 개수
    dic = {gems[0]: 1, }
    start, end = 0, 0

    while start < len(gems) and end < len(gems):
        if len(dic) < kind:  # 종류 부족하면 end point 증가 & dic 개수 증가
            end += 1
            if end == len(gems):
                break
            dic[gems[end]] = dic.get(gems[end], 0)+1

        else:  # 종류 같으면 ans 비교 후 답 갱신하고, start point 증가 & dic 개수 다운
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

    return [answer[0]+1,answer[1]+1]