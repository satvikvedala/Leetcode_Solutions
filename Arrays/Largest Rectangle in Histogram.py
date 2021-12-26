class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
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
