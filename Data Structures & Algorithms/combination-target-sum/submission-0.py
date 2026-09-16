class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # base cases
            if total == target:
                res.append(cur.copy())   # copy! 
                return
            if i >= len(nums) or total > target:
                return

            # choice 1: include nums[i] (reuse allowed → stay at i)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            # choice 2: exclude nums[i] (move on)
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

            
