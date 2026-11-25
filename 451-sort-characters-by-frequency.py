class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        buckets = [[] for _ in range(len(s)+1)]
        for char, count in freq.items():
            buckets[count].append(char)
        
        res = []
        for count in range(len(buckets)-1, 0, -1):
            for char in buckets[count]:
                res.append(char*count)

        return "".join(res)

        

