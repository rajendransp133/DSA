class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx_area=0
        visited_set=set()
        checks=[(0,1),(0,-1),(1,0),(-1,0)]
        m=len(grid)
        n=len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and (i,j) not in visited_set):
                    Q=[(i,j)]
                    visited_set.add((i,j))
                    count=1
                    while(Q):
                        return_val=Q.pop(0)
                        for k in checks:
                            x=return_val[0]+k[0]
                            y=return_val[1]+k[1]
                            if((0<=x<m) and (0<=y<n) and grid[x][y]==1 and (x,y) not in visited_set):
                                Q.append((x,y))
                                visited_set.add((x,y))
                                count+=1
                    maxx_area=max(maxx_area,count)

        return maxx_area
