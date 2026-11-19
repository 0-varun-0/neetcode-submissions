class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        for i in nums:
            a[i] += 1
        heap = []
        for num , count in a.items():
            heapq.heappush(heap , (count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _ , num in heap]
        