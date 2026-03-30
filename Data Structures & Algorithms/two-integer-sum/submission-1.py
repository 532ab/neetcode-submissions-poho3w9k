class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i, value in enumerate(nums):
            diff = target - value
            if diff in result:
                return [result[diff], i]
            result[value] = i
            