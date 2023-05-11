""" 
https://leetcode.com/problems/k-closest-points-to-origin/
원점에 K번째로 가까운 점

문제
평면 상에 points 목록이 있을 때. 원점 (0, 0)에서 K번 가까운 점 목록을 순서대로 출력하라. 
평면상 두 점의 거리는 유클리드 거리(각 좌표의 거리의 차를 제곱해서 더한 값의 제곱근)로 한다.

입출력1
입력: points=[[1,3],[-2,2]], k = 1
출력: [[-2,2]]

입출력2
입력: points=[[3,3],[5,-1],[-2,4]], k = 2
출력: [[3,3], [-2, 4]] 
"""
# 틀린 풀이 - 반례로 같은 좌표값이 여러개 나올 수 있다.
# 해당 풀이는 중복되지 않은 좌표값들이 같은 거리 값을 갖을 수 있는 경우만 고려했음
from collections import *
class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 0,0 에서 최대한 가까운 점을 k 개 찾는 것으로 거리를 구하는 공식(유클리드 거리) 를 이용해서 거리를 구한 다음
        # 최대한 가까운 점 k 개는 주어진 좌표들과  0,0 의 거리가 중복되지 않는 k개의 거리가 max값으로 갖을 수 있기 때문에
        # 주어진 좌표 값과 거리를 구해서 오름차 순으로 정렬한 뒤 k 개 만큼만 사용
        distance = sorted(list({int(((0-item[0])**2 + (0-item[1])**2) ** 1/2) for item in points}))[:k]

        # 최대한 가까운 k개의 좌표를 가질 list - return 값
        answer = []

        # key - value로 빠르게 좌표와 그에 해당되는 거리를 찾기 위해 만든 dict
        dtemp = dict()
       
       # 주어진 좌표를 순회화면서 거리를 구하고 이 거리가 max로 가질 수 있는 최소 거리에 있다면
       # 그 좌표값을 key로 거리를(이 때 key값으로 list로 가질 수 없으므로 문자열로 형 변환) value로 해서 dtemp 에 삽입
        for item in points:
            if int(((0-item[0])**2 + (0-item[1])**2) ** 1/2) in distance:
                dtemp[str(item)] = int(((0-item[0])**2 + (0-item[1])**2) ** 1/2)

        # dtemp 를 value값(key(좌표)가 가진 0,0 과의 거리를 기준으로 오름차순 정렬하고 중복된 거리값을 갖는 경우가 있기 때문에 해당
        # 좌표값을 k개만큼만 사용하기 위해서 k개까지 자르고 해당되는 key값(좌표들)을 반환해서 list로 변환
        answer = list(dict(sorted(dtemp.items(), key = lambda item: item[1])[:k]).keys())

        # list로 변환한 answer 에 대해서 answer[i]에 대해서 eval함수로 str로 변환한 `[x, y]`를 다시 list로 변환
        for i in range(len(answer)):
            answer[i] = eval(answer[i])
       
       
        return answer

# 우선 순위 큐 - 최소 heap 을 이용한 풀이
# 파이썬의 heap 을 사용하기 위해서 라이브러리 import
import heapq
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 최소 힙으로 사용하기 위해 heap 선언 (파이썬에서는 일반 힙이 최소힙)
        heap = []
        # 결과인 좌표값들을 반환할 list
        answer = []
        
        # 주어진 좌표값들에 대해서 순회하면서 heap에 [(거리, [x, y]), (거리, [Z, r]), ... ] 로 힙에 삽입
        for item in points:
            heapq.heappush(heap, (int(((0-item[0])**2 + (0-item[1])**2) ** 1/2), item))
        
        # 생성한 heap이 숫자인 거리에 값을 기준으로 heap[1]에 해당되는 좌표값을 0,0과의 거리가 작은 값부터 pop해서 answer에 차례대로
        # 삽입
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
       
        return answer