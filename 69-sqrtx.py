class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1, x
        ans = 1

        if x == 0:
            return 0

        while l <= r:
            m = l + ((r-l)//2)
            sq = m * m

            if sq == x:
                return m
            elif sq < x:
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans

            