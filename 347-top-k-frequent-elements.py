class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        freq = defaultdict(list)
       
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            

        res = sorted(freq, key=lambda x:(-freq[x],x))

       
        return res[:k]
            

       
        