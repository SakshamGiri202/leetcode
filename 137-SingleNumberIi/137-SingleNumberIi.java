// Last updated: 10/2/2026, 10:11:17 AM
class Solution {
    public int singleNumber(int[] nums) {
         int ones = 0, twos = 0;

        for (int num : nums) {
            ones = (ones ^ num) & ~twos;
            twos = (twos ^ num) & ~ones;
        }

        return ones;
    }
    
}