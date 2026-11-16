class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for i in strs:
            s = tuple(i.count(c) for c in "abcdefghijklmnopqrstuvwxyz")
            a[s].append(i)
        return list(a.values()) 

        