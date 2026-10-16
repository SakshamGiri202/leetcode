class Solution:

    def frequencySort(self, nums: list[int]) -> list[int]:
        n = len(nums)

        groups = {}

        for i in nums:
            groups[i] = groups.get(i, 0) + 1

        
        pairs = []

        for item, count in groups.items():
            pairs.append((item, count))

        pairs.sort(key=lambda x: (x[1], -x[0]))

        res = []

        for item, count in pairs:
            res.extend([item]*count)


        return res

        