class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx_area=0
        visited_set=set()
        checks=[(0,1),(0,-1),(1,0),(-1,0)]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==0):
                    visited_set.add((i,j))
        
        for i in range(m):
            for j in range(n):
                count=0
                if(grid[i][j]==1 and (i,j) not in visited_set):
                    Q=[(i,j)]
                    maxx_area=max(1,maxx_area)
                    while(Q):
                        return_val=Q.pop(0)
                        print(return_val,Q)
                        for k in checks:
                            x=return_val[0]+k[0]
                            y=return_val[1]+k[1]
                            if((0<=x<m) and (0<=y<n) and (x,y) not in visited_set):
                                Q.append((x,y))
                                visited_set.add((x,y))
                                count+=1
                maxx_area=max(maxx_area,count)

        return maxx_area
