class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area= 0
        n = len(height)
        i = 0
        j = n -1
        while i < j:
            h = min(height[i], height[j])
            w = abs(i-j)
            area = h * w

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
            max_area = max(area, max_area)
        return max_area
