class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while len(heap) > 1:
            stone_x = heapq.heappop_max(heap)
            stone_y = heapq.heappop_max(heap)
            if stone_x == stone_y:
                continue
            heapq.heappush_max(heap, abs(stone_x - stone_y))
        return heap[0] if heap else 0