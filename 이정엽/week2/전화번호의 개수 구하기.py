# 2차원 배열

# # def solution(num):

# list1 = [0,0,0,0]
# list1.append()
# a, b, c, d = map(int, input().split()) 
# # a, b = num.split('')
# nums = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
# # nums1 = []
# # result1 = []
# # for i in list(nums[a-2]):
# #     for j in list(nums[b-2]):
# #         a = ''.join(i+j)
# #         result1.append(a)
# # print(result1)
#     # return result1

# # print(solution(23))

# iterator1 = list(nums[a-2])
# iterator2 = list(nums[b-2])
# iterator3 = list(nums[c-2])
# iterator4 = list(nums[d-2])
# if a == 0:
#     iterator1 = []
# elif b == 0:
#     iterator2 = []


# # a = list(product(iterator1, iterator2))
# # print(a)
# # answer = ''.join(map(str,a))
# # print([(i,j) for i in iterator1 for j in iterator2])

# a = [''.join(map(str, (i,j,k,l))) for i in iterator1 for j in iterator2 for k in iterator3 for l in iterator4]
# print(a)



# ^ 위의 식들은 4개의 값이 주어졌을때 오류가 발생하며 발생하지 않도록 하기 위해서 for문을 사용하면 상당히 비효율적으로 판단하였다.

from itertools import product

# 밑부터는 다시풀었는 것 
# 밑에 수식은 product를 사용하여 각 값을 하나하나 비교하여 주었더.
def solution(n):
    list1 = list(n)
    if len(list1) == 0: # ''가 입력이 되면 [] 값을 리턴한다.
        return []
    list3 = []
    list5 = []
    nums = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'] 
    for i in list1:  
        i = int(i)
        list2 = list(nums[i-2]) # list2에 nums요소를 하나의 리스트로 만든다.
        list3.append(list2)     # list3에 list3의 요소를 포함한ㄷ.
    a = list(product(*list3))
    for i in a:
        b = ''.join(i)      #list3안에 있는 요소 하나하나를 조인하여 없애준다.
        list5.append(b)
    return list5

s = '345'
print(solution(s))

