class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0 
        for i in grid:
            for j in sorted(i):
                if j >= 0:
                    break
                count += 1
        return count