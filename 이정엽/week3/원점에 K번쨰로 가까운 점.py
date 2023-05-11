# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#             return sorted(points, key = lambda x: (x[0]-0)**2 + (x[1]-0)**2)[:k]
#---------위는 리트코드 정답이다...

        
def solution(points, k):
    my_dict = {}
    for i in points:
        x, y = i  # x, y 변수에 i 리스트의 요소를 대입
        dic_value = x**2 + y**2
        my_dict[tuple(i)] = abs(dic_value)  # i 값을 key로, dic_value 값을 value로 하는 쌍을 추가
    # value 값 기준으로 정렬하고, 상위 k개의 point를 추출
    sorted_points = sorted(my_dict, key=lambda x: my_dict[x])[:k] 
    # 뒤의 값을 오름차순으로 정렬한 리스트 반환
    return sorted(sorted_points, key=lambda x: x[1])

s = [[3,3], [5,-1],[-2,4]]

n = 2

print(solution(s, n))