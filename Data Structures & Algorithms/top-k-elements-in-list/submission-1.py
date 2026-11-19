class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        for i in nums:
            a[i] += 1
        
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        for num , count in a.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets)-1 , 0 , -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k :
                    return res
        return res
        