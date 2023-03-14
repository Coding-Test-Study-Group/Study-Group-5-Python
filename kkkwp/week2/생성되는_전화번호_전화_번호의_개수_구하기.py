# 시간 복잡도 O(4^n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        answer = []

        # digits의 길이가 0이면 빈 배열 반환
        if not digits:
            return []

        def dfs(idx, cur):
            # 끝까지 왔으면 answer에 넣어서 반환
            if idx == len(digits):
                answer.append(cur)
            else:
                # digit의 각 숫자를 phone에서 찾아서 해당하는 ch를 가져온다.
                for ch in phone[digits[idx]]:
                    # 현재 문자열 cur에 ch를 덧붙여서 또다시 dfs를 돈다.
                    # 더 갈 수 있을 때까지 계속해서 반복 -> 위의 if문 만나면 더 못 가고 정답 배열에 넣기
                    dfs(idx + 1, cur + ch)

        dfs(0, "")
        return answer