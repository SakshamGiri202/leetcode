class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        1st approach:
        step 1: first we'll find the no's of rows and cols and then
        step 2: loop then to find the row where target is located
        step 3: if target is not found in the entire rows then return false 
        step 4: after find the specific row then loop through them to find the target
        """
        row, col = len(matrix), len(matrix[0])

        left, right = 0, row - 1

        # find the row the contains target elements
        while left <= right:
            mid_row = (left+right)//2
            if target > matrix[mid_row][-1]:
                left = mid_row + 1
            elif target < matrix[mid_row][0]:
                right = mid_row - 1
            else:
                break
        
        if not (left <= right):
            return False
        
        # now loop through the row to find the target
        mid_row = (left+right)//2
        l, r = 0, col - 1

        while l <= r:
            m = (l+r)//2
            if target > matrix[mid_row][m]:
                l = m + 1
            elif target < matrix[mid_row][m]:
                r = m - 1
            else:
                return True

        return False


       


    
