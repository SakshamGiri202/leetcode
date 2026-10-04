# Last updated: 10/4/2026, 11:29:38 PM
class Solution:
    def getLeftMax(self,h:list[int], n:int) -> list[int]:
        leftMax = [0]*n
        leftMax[0] = h[0]
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], h[i])
        return leftMax

    def getRightMax(self, h:list[int], n:int) -> list[int]:
        rightMax = [0]*n
        rightMax[n-1] = h[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], h[i])
        return rightMax

    def trap(self, height: list[int]) -> int:
        n = len(height)
        sum = 0
        leftMax = self.getLeftMax(height, n)
        rightMax = self.getRightMax(height, n)
        for i in range(n):
            out = min(leftMax[i], rightMax[i]) - height[i]
            sum += out
        return sum

