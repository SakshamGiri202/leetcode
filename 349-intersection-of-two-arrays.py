class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []

        for n1, n2 in zip(nums1, nums2):
            if len(nums1) > len(nums2):
                if n2 in nums1:
                    res.append(n2)
            else:
                if n1 in nums2:
                    res.append(n1)

        return list(set(res))