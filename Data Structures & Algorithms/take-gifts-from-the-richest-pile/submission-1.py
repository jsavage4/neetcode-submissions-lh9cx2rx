class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        while k > 0:
            gift = heapq.heappop(gifts)
            heapq.heappush(gifts, -int(sqrt(-gift)))
            k -= 1
        print(gifts)
        return -sum(gifts)