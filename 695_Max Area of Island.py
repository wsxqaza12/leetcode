class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()

        def getSize(x, y):
            if (x < 0 or x == ROW or y < 0 or y == COL or
                    grid[x][y] == 0 or (x, y) in visit):
                return 0
            visit.add((x, y))
            return (1 + getSize(x + 1, y) +
                    getSize(x - 1, y) +
                    getSize(x, y + 1) +
                    getSize(x, y - 1))

        max_size = 0
        for i in range(ROW):
            for j in range(COL):
                curr = getSize(i, j)
                max_size = max(max_size, curr)

        return max_size
