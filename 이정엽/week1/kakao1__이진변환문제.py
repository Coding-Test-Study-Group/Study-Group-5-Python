def solution(s):   
    cnt = 0
    sum = 0
    while s != "1": 
        num1 =s.count('0') #0의 갯수를 카운트하고
        str = s.replace('0', '') #0을 없앤다
        num2= len(str) #길이를 측정하여 
        s = bin(num2)[2:] #2진수로 변환하는데 2:를 통하여 앞에 0b라는 부분을 제거한다.
        cnt += 1 # 횟수 확인
        sum += num1 # 0의 갯수를 구한다.
    
    list = [cnt, sum]
    return list
