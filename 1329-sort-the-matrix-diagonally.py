class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        n = len(mat)
        m =len(mat[0]) if n > 0 else 0

        mp = {}
       

        for i in range(n):
            for j in range(m-1,-1, -1):
                key = i - j
                if key not in mp:
                    mp[key] = []
                mp[key].append(mat[i][j])
        
        for key in mp:
            mp[key].sort()

        for i in range(n):
            for j in range(m-1, -1, -1):
                key = i - j
                mat[i][j] = mp[key].pop(0)
        
        return mat

            

