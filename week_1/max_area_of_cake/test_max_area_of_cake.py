import unittest
from max_area_of_cake import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        h = 5
        w = 4
        horizontalCuts = [1,2,4]
        verticalCuts = [1,3]
        self.assertEqual(self.solution.maxArea(h, w, horizontalCuts, verticalCuts), 4)

    def test_example_2(self):
        h = 5
        w = 4
        horizontalCuts = [3,1]
        verticalCuts = [1]
        self.assertEqual(self.solution.maxArea(h, w, horizontalCuts, verticalCuts), 6)

    def test_example_3(self):
        h = 5
        w = 4
        horizontalCuts = [3]
        verticalCuts = [3]
        self.assertEqual(self.solution.maxArea(h, w, horizontalCuts, verticalCuts), 9)
