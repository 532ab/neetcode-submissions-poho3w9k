class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDupl = False
        for i in range(len(nums)):
            value = nums[i]
            for j in range(i + 1, len(nums)):
                if(value == nums[j]):
                    hasDupl = True
        return hasDupl           

        