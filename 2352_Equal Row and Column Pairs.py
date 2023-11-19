class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}
        n = len(grid)

        for i in range(n):
            row = grid[i]
            row = str(row)
            if row not in d:
                d[row] = 1
            else:
                d[row] += 1

        pair = 0
        for i in range(n):
            col = [row[i] for row in grid]
            col = str(col)
            if col in d:
                pair += d[col]

        return pair
