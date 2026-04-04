class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequency = Counter(nums)
        for num, count in frequency.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        ret = []
        print(heap)
        for val in range(len(heap)):
            ret.append(heapq.heappop(heap)[1])

        return ret