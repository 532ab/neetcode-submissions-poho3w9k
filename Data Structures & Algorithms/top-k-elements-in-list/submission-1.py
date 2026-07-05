class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        while len(res) < k:
            maxNum = None
            maxFreq = 0

            for n in freq:
                if freq[n] > maxFreq:
                    maxFreq = freq[n]
                    maxNum = n

            res.append(maxNum)
            freq.pop(maxNum)

        return res
