def solution(s):
    stage = 0
    zero = 0
    while True:
        if s == "1":
            break
        for ch in s:
            if ch == "0":
                zero += 1
                s = s.replace(ch, "")
        s = bin(len(s))[2:]
        stage += 1
    return [stage, zero]