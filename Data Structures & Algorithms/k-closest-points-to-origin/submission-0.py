from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]