# 1번째 방법
# 입력값의 범위가 작아서 문자열 조합으로 풀어봤음
# Runtime: 35ms, Memory Usage: 13.9MB
def Solution(digits):
        h = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

        answer = []

        if len(digits) == 0:
            return answer
        if len(digits) == 1:
            return h[digits]
        answer = h[digits[0]]
        for i in range(1, len(digits)):
            a = answer
            b = h[digits[i]]
            tmp = []
            for j in a:
                for k in b:
                    tmp.append(j + k)
            answer = tmp
        return answer

# 2번째 방법
# 백트래킹
# Runtime: 31ms, Memory Usage: 13. MB
def Soulution(digits):
    if not digits:
        return []
    
    nums = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

    answer = []
    
    def func(index, currentString):
        if index == len(digits):
            answer.append(currentString)
        else:
            for letter in nums[digits[index]]:
                func(index + 1, currentString + letter)
    func(0, '')
    
    return answer