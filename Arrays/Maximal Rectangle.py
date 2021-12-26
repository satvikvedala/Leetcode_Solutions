class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def func(arr):
            stack = []
            maxarea = 0
            i = 0
            while i<len(arr):
                if len(stack) == 0 or arr[i]>arr[stack[-1]]:
                    stack.append(i)
                    i+=1
                else:
                    temp = stack.pop()
                    maxarea = max(maxarea,arr[temp]*((i-stack[-1]-1) if stack else i))
            while stack:
                temp = stack.pop()
                maxarea = max(maxarea,arr[temp]*((i-stack[-1]-1)if stack else i))
            return maxarea
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]) == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j]+int(matrix[i][j])
        maxarea = 0
        for i in range(len(matrix)):
            maxarea = max(maxarea,func(dp[i]))
        return maxarea
