from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, r: int, c: int, cells: List[List[int]]) -> int:
        
        def canCross(day: int) -> bool:
            grid = [[0] * c for _ in range(r)]
            for i in range(day):
                x, y = cells[i]
                grid[x - 1][y - 1] = 1
            
            q = deque()
            visited = [[False] * c for _ in range(r)]
            
            for j in range(c):
                if grid[0][j] == 0:
                    q.append((0, j))
                    visited[0][j] = True
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while q:
                x, y = q.popleft()
                if x == r - 1:
                    return True  
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        if not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            q.append((nx, ny))
            
            return False
        
        left, right = 0, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
