def solution(s):
    count = 0
    zero =0
    
    while len(s) > 1:
        new = s.replace("0","")
        zero += len(s) - len(new)
        count += 1
        s = bin(len(new))[2:]

    print([count, zero])

solution("110010101001")