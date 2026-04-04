class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_a = heapq.heappop(stones)
            stone_b = heapq.heappop(stones)
            if stone_a != stone_b:
                heapq.heappush(stones, -abs(stone_a - stone_b))
        
        return abs(stones[0]) if stones else 0