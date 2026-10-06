class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n <= 1:
            return
        
        # find the pivot element
        pivot = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        # if pivot element is not found
        if pivot == -1:
            nums.reverse()
            return

        # swap the element if pivot is found
        for i in range(n-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        # if the element after pivot is in ascending sort then
        left = pivot+1
        right = n-1 

        while right>left:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
    
                    