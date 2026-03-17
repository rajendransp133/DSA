class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        check=[(0,1),(-1,0),(1,0),(0,-1)]

        perimeter=0

        for row in range(m):
            for j in range(n):
                if(grid[row][j]>0):
                    dum_sum=4
                    for k in check:
                        if(0<=row+k[0]<m and 0<=j+k[1]<n and grid[row+k[0]][j+k[1]]>0):
                            dum_sum-=1
                    perimeter+=dum_sum

        return perimeter

