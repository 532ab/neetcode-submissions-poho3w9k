class Solution {
    public boolean hasDuplicate(int[] nums) 
    {
        int value = 0;
        for(int i = 0; i < nums.length; i++)
        {
            value = nums[i];
            for(int j = i + 1; j < nums.length; j++)
            {
                if(value == nums[j])
                {
                    return true;
                }
            }
        }
        return false;
    }
}