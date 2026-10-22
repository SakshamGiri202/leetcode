class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        length = 0
        odd = 0
        mp = {}
        hasOdd = False
        for i in s:
            mp[i] =mp.get(i, 0) + 1

        print(mp)

        for val in mp.values():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1
                hasOdd = True
              

        if hasOdd:
            length += 1
    
        return length            