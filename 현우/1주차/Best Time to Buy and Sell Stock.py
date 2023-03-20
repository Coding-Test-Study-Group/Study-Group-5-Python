from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 최대 이익
        max_profit = 0

        # 주식의 최저가
        # 초기값으로 제한 사항의 최대값을 설정
        min_price = 10000

        for price in prices:
            # 현재 주가와 최저가를 비교하여 최솟값을 저장
            min_price = min(price, min_price)

            # 이익: 현재 주가에서 최저가를 뺀 가격
            profit = price - min_price

            # 최대 이익: 현재 이익과 지금까지의 이익을 비교하여 최대값을 저장
            max_profit = max(profit, max_profit)

        return max_profit


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(Solution().maxProfit(prices=[7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
