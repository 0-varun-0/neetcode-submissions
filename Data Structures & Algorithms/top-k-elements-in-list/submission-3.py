class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_freq = max(freq.values())

        buckets: List[List[int]] = [[] for _ in range(max_freq + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        res: List[int] = []
        for count in range(max_freq, 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res

        return res