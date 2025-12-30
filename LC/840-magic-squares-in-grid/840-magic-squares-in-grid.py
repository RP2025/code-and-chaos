class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if R < 3 or C < 3:
            return 0
        base = [
            [8, 1, 6],
            [3, 5, 7],
            [4, 9, 2]
        ]

        def rotate(square):
            return [list(row) for row in zip(*square[::-1])]

        def reflect(square):
            return square[::-1]
        valid_patterns = set()
        curr = base
        for _ in range(4):
            valid_patterns.add(tuple(num for row in curr for num in row))
            valid_patterns.add(tuple(num for row in reflect(curr) for num in row))
            curr = rotate(curr)

        count = 0

        for r in range(R - 2):
            for c in range(C - 2):
                if grid[r + 1][c + 1] != 5:
                    continue

                subgrid = (
                    grid[r][c],     grid[r][c + 1],     grid[r][c + 2],
                    grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                    grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]
                )

                if subgrid in valid_patterns:
                    count += 1

        return count
