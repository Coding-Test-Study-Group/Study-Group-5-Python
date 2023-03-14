import unittest


def solution(s):
    # 변환 횟수를 저장할 변수
    transform_cnt = 0
    # 제거할 0의 개수를 저장할 변수
    remove_zero_cnt = 0

    # s가 "1"이 될 때까지 반복
    while s != "1":
        # 제거할 0의 개수
        remove_zero_cnt += s.count("0")

        # 0 제거
        new_s = s.replace("0", "")

        # 0 제거 후 길이
        len_new_s = len(new_s)

        # 이진 변환 결과
        s = format(int(len_new_s), "b")

        # 변환 횟수 카운트
        transform_cnt += 1

    answer = [transform_cnt, remove_zero_cnt]

    return answer


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(s="110010101001"), [3, 8])
        self.assertEqual(solution(s="01110"), [3, 3])
        self.assertEqual(solution(s="1111111"), [4, 1])


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
