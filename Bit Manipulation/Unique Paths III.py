class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.arr1 = [-1,0,1,0]
        self.arr2 = [0,1,0,-1]
        def isSafe(x,y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]==-1:
                return False
            return True
        def func(grid,x,y,zero_count,count):
            #print(x,y,zero_count,grid[x][y],count[0],isSafe(x,y))
            if grid[x][y] == 2:
                if zero_count == 0:
                    count[0]+=1
                return
            else:
                for i,j in zip(self.arr1,self.arr2):
                    x1 = x+i
                    y1 = y+j
                    if isSafe(x1,y1) and (grid[x1][y1] == 0):
                        temp = grid[x1][y1]
                        grid[x1][y1] = 1
                        zero_count-=1
                        func(grid,x1,y1,zero_count,count)
                        grid[x1][y1] = temp
                        zero_count+=1
                    elif isSafe(x1,y1) and grid[x1][y1] == 2:
                        func(grid,x1,y1,zero_count,count)
            #print(x,y,zero_count,grid[x][y],count[0])
            #print("************************************")
                        
                    
        count = [0]
        zero_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zero_count+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    func(grid,i,j,zero_count,count)
        return count[0]
                    
