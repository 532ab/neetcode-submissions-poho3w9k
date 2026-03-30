class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {}
        most = float('-inf')
        result = 0

        for i in range(len(nums)):
            track[nums[i]] = 1 + track.get(nums[i], 0)
           

        for key, value in track.items():
            if value > most:
                most = value
                result = key
        
        return result
            
