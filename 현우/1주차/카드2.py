import unittest
from collections import deque


def solution(n):
    queue = deque([_ for _ in range(1, n + 1)])

    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())

    return queue[0]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(n=6), 4)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
