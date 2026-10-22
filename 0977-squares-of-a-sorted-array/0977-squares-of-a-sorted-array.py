class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # res=[abs(x) for x in nums]
        # res.sort()
        # return [x*x for x in res]
        return sorted([x*x for x in nums])