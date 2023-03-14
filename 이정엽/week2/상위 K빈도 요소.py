def solution(nums, k):
    list1 = []
    for i in nums:
        if nums.count(i) >= k:
            list1.append(i)
    
    # result1 = dict.fromkeys(list1) // 기존의 리스트의 순서를 유지하고 중복을 제거할 수 있으나, 출력 값이 {1: None, 2: None} dice로 구현이 된다.
    # result2 = list(result1) // 위 주석 처리된 방법으로 중복을 제거 하려하였으나 비효율적이라고 판단하였다.
    result2 = list(set(list1))
    return result2
    

nums = [1,1,1,2,2,3] 
k = 2
print(solution(nums, k))