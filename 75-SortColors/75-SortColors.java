// Last updated: 10/2/2026, 10:11:18 AM
class Solution {
    public void sortColors(int[] nums) {
        for(int i = 0; i < nums.length - 1; i++){
            int min_idx = i;
            for(int j = i +1; j < nums.length; j++){
                if(nums[j]<nums[min_idx]){
                    min_idx = j;
                }
            }
            int temp = nums[i];
            nums[i] = nums[min_idx];
            nums[min_idx]=temp;
        }
    }
}