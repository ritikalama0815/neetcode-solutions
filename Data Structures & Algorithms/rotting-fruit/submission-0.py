class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        rotten = collections.deque()

        #keep the track of fresh fruits and minutes elapsed
        time, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    rotten.append((r,c))
        
        while fresh > 0 and rotten:
            numberRotten = len(rotten)
            for i in range(numberRotten):
                r,c = rotten.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row in range(rows)
                        and col in range(cols)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        rotten.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

                    