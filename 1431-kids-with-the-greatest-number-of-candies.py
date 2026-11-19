class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        # 1st approach using hashmap and array
        # n = len(candies)

        # res = [] * n

        # mp = {}

        # for i in range(n):
        #     mp[i] = candies[i] 

        # max_val = max(mp.values())


        # for i in range(n):

        #     if mp[i] + extraCandies < max_val:
        #         res.insert(i, False)
        #     else:
        #         res.insert(i, True)

        # return res
        

        # 2nd approach using array

        res = []

        for candie in candies:
            if candie + extraCandies < max(candies):
                res.append(False)
            else:
                res.append(True)

        return res