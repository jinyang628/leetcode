class Solution {
    public int[] rearrangeArray(int[] nums) {
        boolean a = nums[0]<nums[1];   //Using this boolean to decide the order of elements
        for(int i=1;i<nums.length-1;i++){
            if((a && nums[i]<nums[i+1]) || (!a && nums[i]>nums[i+1])){   //Swapping elements based on boolean 'a' and current order of adjacent elements
                int t = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = t;
            }
            a=!a;    //Toggling the order of elements to increasing/decreasing at every iteration
        }
        return nums;
    }
}