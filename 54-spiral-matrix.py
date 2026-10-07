class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
            
        # 1. Initialize boundary indices (not the matrix values!)
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []
        
        # 2. Loop until boundaries cross over
        while left <= right and top <= bottom:
            # Move Right: Traverse top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1 # Shrink top boundary
            
            # Move Down: Traverse rightmost column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1 # Shrink right boundary
            
            # Check if boundaries crossed after shrinking top/right
            if top <= bottom:
                # Move Left: Traverse bottom row
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1 # Shrink bottom boundary
                
            if left <= right:
                # Move Up: Traverse leftmost column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1 # Shrink left boundary
                
        return res
