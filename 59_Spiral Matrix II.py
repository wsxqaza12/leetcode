class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        num = 1
        row = 0
        col = 0
        direction_row = [0, 1, 0, -1]
        direction_col = [1, 0, -1, 0]
        direction_state = 0

        while num <= n*n:
            matrix[row][col] = num
            nextRow = row + direction_row[direction_state]
            nextCol = col + direction_col[direction_state]

            if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= n or matrix[nextRow][nextCol] != 0:
                direction_state = (direction_state+1) % 4
            
            num += 1
            row += direction_row[direction_state]
            col += direction_col[direction_state]
        
        return matrix