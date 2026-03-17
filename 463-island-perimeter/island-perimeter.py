class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        grid_copy = [[i * 4 for i in row] for row in grid]
        m=len(grid)
        n=len(grid[0])

        check=[(0,1),(-1,0),(1,0),(0,-1)]

        perimeter=0

        for row in range(m):
            for j in range(n):
                if(grid[row][j]>0):
                    for k in check:
                        if(0<=row+k[0]<m and 0<=j+k[1]<n):
                            if(grid[row+k[0]][j+k[1]]>0):
                                grid_copy[row][j]-=1
                perimeter+=grid_copy[row][j]

        return perimeter

