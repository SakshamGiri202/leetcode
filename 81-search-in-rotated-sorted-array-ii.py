class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = (r+l)//2

            if nums[m] == target:
                return True

            # if encountes any duplicate elements than increment left half and decrement right half
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue

            # check if the left side is sorted and eliminate right side
            if nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # or check if the right side is sorted and eliminate lift side
            else:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False