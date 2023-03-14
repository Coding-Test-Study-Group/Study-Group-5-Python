from collections import Counter

def Solution(nums, k):
    N = Counter(nums).most_common(k)
    answer = [i[0] for i in N]
    print(answer)

Solution([1,1,1,2,2,3], 2)