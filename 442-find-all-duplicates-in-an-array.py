class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        
        # 1st approach using hashmap
        # mp = {}

        # res = []

        # if nums is None and nums == 1:
        #     return res

        # for num in nums:
        #     mp[num] = mp.get(num, 0) + 1


        # for key, val in mp.items():
        #     if val == 2:
        #         res.append(key)

        # return res

        # 2nd approach using set hashmap

        seen = set()

        res = []

        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen.add(num)

        return res