# k개 이상 존재하는 문자를 반환하는 것이 아니라
# 리스트 내에서 순서대로(상위) k 개의 문자를 반환하는 것(중복X)
from collections import *
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        cnt = Counter(nums).most_common(k)
        for i in range(len(cnt)):
            result.append(cnt[i][0])
        return result