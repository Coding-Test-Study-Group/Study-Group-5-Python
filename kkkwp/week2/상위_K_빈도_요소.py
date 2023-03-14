from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = Counter(nums).most_common(k)
        return [i[0] for i in top]