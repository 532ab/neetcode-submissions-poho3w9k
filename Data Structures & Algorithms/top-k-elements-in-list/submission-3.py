class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            track[nums[i]] = 1 + track.get(nums[i], 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for i, n in track.items():
            buckets[n].append(i)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k :
                    return res
