class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res = 0

        n = len(nums)
        sum = 0
        mp = {0: 1}

        for i in range(n):
            sum += nums[i]
             
            rem = sum % k

            if rem not in mp:
                mp[rem] = mp.get(rem, 0) + 1
            else:
                if rem < 0:
                    rem += k 
                res += mp[rem]
                mp[rem] += 1

        return res