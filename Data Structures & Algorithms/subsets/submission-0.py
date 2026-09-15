class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        currSub = []

        def dfs(i):
            if i >= len(nums):
                res.append(currSub.copy())
                return
            currSub.append(nums[i])
            dfs(i+1)
            currSub.pop()
            dfs(i+1)
        
        dfs(0)
        return res
            
