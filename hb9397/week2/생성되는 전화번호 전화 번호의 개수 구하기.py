class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        tel = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}        
        result = []

        # digits 의 가능한 최소 inedx 와 조합할 문자열을 저장할 path
        def bt(index, char):
            # 조합된 문자열 길이가 입력 받은 digits 의 길이와 같다면 조합이 완료된 것으로 result에 현재 조합된 문자열 추가
            if len(char) == len(digits):
                result.append(char)
                return

            # i 는 현재 digits[i]의 indedx 부터 digits의 끝까지에 해당되는 index를 가리킨다.
            for i in range(index, len(digits)):
                # 현재 digits[i] 가 가질 수 있는 모든 문자열에 대해서 
                for item in tel[int(digits[i])]:
                    # digitis[i] 로 가능한 문자를 path + item 으로 새로운 문자열 조합을 만들어주고.
                    # digits[i] 로 가능한 문자열 중 맨 앞 문자 하나를 들고 digitis[i+1] 에 접근해서 반복
                    bt(i+1, char + item)

        bt(0, '')

        # 입력된 숫자 다이얼이 없는 경우 결과의 출력에 대한 형식을 맞추기 위해서 예외처리
        if digits == "":
            result = []

        return result