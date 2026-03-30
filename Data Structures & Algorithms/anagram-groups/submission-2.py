class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        final = defaultdict(list)

        for i in strs:
            result = "".join(sorted(i))
            final[result].append(i)
        return list(final.values())
