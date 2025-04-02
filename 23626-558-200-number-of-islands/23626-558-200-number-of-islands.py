class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Depth first search 

        num_islands = 0
        rows = len(grid)
        columns = len(grid[0])

        def dfs(row, column):
            
            if row >= rows or row < 0 or column >= columns or column < 0 or grid[row][column] != '1':
                return
            else: 
                grid[row][column] = '0'
                dfs(row, column + 1) # right
                dfs(row, column-1) # left
                dfs(row -1, column) # top
                dfs(row +1, column) # bottom

        for row in range(rows): # row = 0
            for column in range(columns): # column = 0
                if grid[row][column] == '1': #grid(0,0)
                    num_islands += 1    # num_islands = 1
                    #helper function for dfs
                    dfs(row, column)
        return num_islands
                