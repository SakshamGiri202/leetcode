
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        mp = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i + j

                if key not in mp:
                    mp[key] = []
                
                mp[key].append(mat[i][j])
            
        ans = []

        for key in mp:
            if key % 2 == 0:
                mp[key].reverse()
                print(mp[key])
            
            for val in mp[key]:
                ans.append(val)

        return ans