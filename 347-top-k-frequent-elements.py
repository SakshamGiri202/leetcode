class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        freq = list()
        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        sorted_keys = list(mp.keys())
        
        sorted_keys.sort(key=lambda x: mp[x], reverse=True)
        count = 0
        for i in sorted_keys:
            if count < k:
                freq.append(i)
                count += 1
            else: 
                break

        return freq
