class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        retArr = []
        heap = []
        idx = 0
        while idx < k - 1:
            heapq.heappush(heap, (-nums[idx], idx))
            idx += 1
        while idx < len(nums):
            heapq.heappush(heap, (-nums[idx], idx))
            while heap[0][1] <= idx - k:
                heapq.heappop(heap)
            retArr.append(-heap[0][0])
            idx += 1
        return retArr