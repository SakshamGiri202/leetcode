class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)

        res, dist = [], []

        # finding out the index of character occurences
        for i in range(n):
            if c == s[i]:
                res.append(i)
        
        # finding out the closest distance from the character occurence
        for j in range(n):
            min_dist = min(abs(j- idx) for idx in res)
            dist.append(min_dist)
                
        return dist