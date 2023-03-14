def solution(s):
    answer = [0, 0]
    temp = ""

    while True:
        if s == "1":
            break
        
        temp = s.replace("0", '')
        answer[1] += len(s) - len(temp)
        s = str(bin(len(temp))).replace("0b",'')
        answer[0] += 1

    return answer