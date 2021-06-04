from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def findMaxDifference(list: List[int], max_size: int) -> int:
            list.append(0)
            list.append(max_size)
            list.sort()
            max_difference = 0
            for i in range(len(list)):
                if i == len(list) - 1:
                    break
                max_difference = max(max_difference, list[i + 1] - list[i])
            return max_difference

        return (findMaxDifference(horizontalCuts, h) * findMaxDifference(verticalCuts, w)) % 1000000007
