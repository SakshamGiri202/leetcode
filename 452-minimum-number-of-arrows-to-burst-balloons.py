class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()

        def overlap(A, B):
            return A[1] >= B[0]

        n = len(points)
        shots = 0
        i = 0 
        while i < n:
            bounds = points[i]
            shots += 1
            j = i + 1
            while j < n and overlap(bounds, points[j]):
                bounds =[points[j][0], min(bounds[1],points[j][1])]
                j += 1
            i = j

        return shots    
                